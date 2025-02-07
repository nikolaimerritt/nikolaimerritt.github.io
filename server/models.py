import secrets
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlmodel import Field, Session, SQLModel, create_engine, Relationship, select
from pydantic import BaseModel
def _create_user_id(bytes=7) -> str:
    return secrets.token_urlsafe(bytes)


class BossSchema(BaseModel):
    id: int
    name: str
    defeated: bool


class AreaSchema(BaseModel):
    id: int
    name: str
    bosses: list[BossSchema]


class UserSchema(BaseModel):
    id: str
    areas: list[AreaSchema]


class User(SQLModel, table=True):
    id: str = Field(primary_key=True, default_factory=_create_user_id)
    areas: list["Area"] = Relationship()

    def to_schema(self) -> UserSchema:
        return UserSchema(id=self.id, areas=[area.to_schema() for area in self.areas])


class Area(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    user_id: str | None = Field(foreign_key="user.id", index=True, default=None)
    user: User | None = Relationship(back_populates="areas")
    name: str = Field()
    bosses: list["Boss"] = Relationship()

    def to_schema(self) -> AreaSchema:
        return AreaSchema(
            id=self.id or -1,
            name=self.name,
            bosses=[boss.to_schema() for boss in self.bosses],
        )


class Boss(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    area_id: int = Field(foreign_key="area.id", index=True, default=None)
    area: Area = Relationship(back_populates="bosses")
    name: str = Field()
    defeated: bool = Field()

    def to_schema(self) -> BossSchema:
        return BossSchema(id=self.id or -1, name=self.name, defeated=self.defeated)