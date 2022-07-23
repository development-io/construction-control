import sqlalchemy
from .base import metadata
import datetime

objects = sqlalchemy.Table(
    "task",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("author_id", sqlalchemy.Integer),
    sqlalchemy.Column("performer_id", sqlalchemy.Integer),
    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("term_in_fact", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("term_to_plan", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)
