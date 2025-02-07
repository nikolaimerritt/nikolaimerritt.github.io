from typing import Annotated
from .models import User, UserSchema, Area, AreaSchema, Boss, BossSchema
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlmodel import Field, Session, SQLModel, create_engine, Relationship, select
from time import sleep

sqlite_file_name = "sheldon-ring.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


@asynccontextmanager
async def _lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


def _get_session():
    with Session(engine) as session:
        yield session


DatabaseSession = Annotated[Session, Depends(_get_session)]


def _validate_user(db: DatabaseSession, request: Request):
    user_id_header = request.headers.get("UserID")
    if not user_id_header:
        raise HTTPException(status_code=404, detail="No UserID header.")

    user = db.get(User, user_id_header)
    if user:
        return user
    else:
        sleep(2)
        raise HTTPException(status_code=404, detail="Not a registered user.")


AuthorizedUser = Annotated[User, Depends(_validate_user)]
app = FastAPI(lifespan=_lifespan)


@app.post("/signup/")
def create_stuff(db: DatabaseSession) -> UserSchema:
    if len(db.exec(select(User)).all()) > 1000:
        raise HTTPException(status_code=400, detail=f"Too many users already. Go away!")

    user = User()
    area = Area(name="Test area")
    user.areas.append(area)
    area.bosses.append(Boss(name="Hello world test boss", defeated=False))
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"user {user.areas}")
    return user.to_schema()


@app.get("/areas")
def get_user(user: AuthorizedUser) -> list[AreaSchema]:
    return [area.to_schema() for area in user.areas]
