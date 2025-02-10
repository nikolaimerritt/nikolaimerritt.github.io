from typing import Annotated
from models import User, UserSchema, Area, AreaSchema, Boss, BossSchema
from new_user import add_areas
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlmodel import Field, Session, SQLModel, create_engine, Relationship, select
from time import sleep

sqlite_file_name = "/sqlite/sheldon-ring.db"
sqlite_url = f"sqlite://{sqlite_file_name}"
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
        sleep(5)
        raise HTTPException(status_code=404, detail="Not a registered user.")


AuthorizedUser = Annotated[User, Depends(_validate_user)]
app = FastAPI(lifespan=_lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*"
)


@app.post("/api/signup")
def create_stuff(db: DatabaseSession) -> UserSchema:
    if len(db.exec(select(User)).all()) > 1000:
        raise HTTPException(status_code=400, detail=f"Too many users already. Go away!")

    user = User()
    add_areas(user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.to_schema()


@app.get("/api/areas")
def get_user(user: AuthorizedUser) -> list[AreaSchema]:
    return [area.to_schema() for area in user.areas]


@app.post("/api/boss/{boss_id}/defeated/{defeated}")
def set_boss_defeated(
    db: DatabaseSession, user: AuthorizedUser, boss_id: int, defeated: bool
) -> BossSchema:
    boss = db.exec(
        select(Boss, Area, User)
        .join(Area, Boss.area_id == Area.id)
        .join(User, User.id == Area.user_id)
        .where(User.id == user.id, Boss.id == boss_id)
    ).first()
    if not boss:
        raise HTTPException(
            status_code=404, detail=f"Could not find a boss with id {boss_id}"
        )
    boss = boss[0]
    boss.defeated = defeated
    db.add(boss)
    db.commit()
    db.refresh(boss)
    return boss.to_schema()
