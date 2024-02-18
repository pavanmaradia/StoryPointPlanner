"""
Database model structure
"""
from database import _sql, BASE
import passlib.hash as _hash


class User(BASE):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    password = _sql.Column(_sql.String)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.password)
