from sqlalchemy.orm import registry

from sandbox.persistence.orm import schema
from sandbox.domain.models.album import Album

mapper_registry = registry()

# Map the domain models to database tables tables
mapper_registry.map_imperatively(Album, schema.t_albums)
