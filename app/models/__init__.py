import sqlalchemy

from ..extensions import db

from .user import User
from .role import Role


sqlalchemy.orm.configure_mappers()
