# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import registry

mapper_registry = registry()


t_albums = Table(
    'albums', mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('artist', String(255), nullable=False)
)


t_songs = Table(
    'songs', mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('album_id', ForeignKey('albums.id'), nullable=False)
)
