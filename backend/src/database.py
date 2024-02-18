"""
Database configuration
"""

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "sqlite:///./database.db"

ENGINE = _sql.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SESSION_LOCAL = _orm.sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

BASE = _declarative.declarative_base()


def add_in_db(db: _orm.Session, obj) -> None:
    db.add(obj)
    db.commit()
    db.refresh(obj)
