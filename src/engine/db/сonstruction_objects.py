import sqlalchemy
from .base import metadata
import datetime

objects = sqlalchemy.Table(
    "task",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("author", sqlalchemy.String),
    sqlalchemy.Column("performer", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("term_in_fact", sqlalchemy.DateTime, default=datetime.datetime.utcnow, nullable=True),
    sqlalchemy.Column("term_to_plan", sqlalchemy.DateTime, default=datetime.datetime.utcnow, nullable=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow, nullable=True),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow, nullable=True),
    sqlalchemy.Column("bot_tg_enabled", sqlalchemy.Boolean),
    sqlalchemy.Column("closed", sqlalchemy.Boolean),
)

authors = sqlalchemy.Table(
    "author",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)

performers = sqlalchemy.Table(
    "performer",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)
