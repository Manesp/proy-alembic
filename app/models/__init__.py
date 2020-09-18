import sqlalchemy

from ..extensions import db

from .user import User


sqlalchemy.orm.configure_mappers()
