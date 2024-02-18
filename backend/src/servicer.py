"""
define all api services
"""
import fastapi.security as _security
import jwt
import passlib.hash as _hash
import models as _models

import sqlalchemy.orm as _orm

import database, models, schemas

OAUTH_SCHEMA = _security.OAuth2PasswordBearer(tokenUrl="api/token")
JWT_SECRET = "ThisIsSecret"


def create_database():
    return database.BASE.metadata.create_all(bind=database.ENGINE)


def get_db():
    db = database.SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()


async def create_user(user: schemas.UserCreate, db: _orm.session):
    user_obj = models.User(email=user.email, password=_hash.bcrypt.hash(user.password))
    database.add_in_db(db, user_obj)
    return user_obj


async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.email == email).first()


async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await get_user_by_email(email=email, db=db)
    if not user:
        return False
    return user


async def create_token(user: _models.User):
    user_obj = schemas.User.from_orm(user)

    token = jwt.encode(user_obj.dict(), JWT_SECRET)

    return dict(access_token=token, token_type="bearer")
