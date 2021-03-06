from sandbox.domain.models.album import Album
from sandbox.domain.repositories.albums import AlbumRepository
from sandbox.persistence.orm.database import db_session


class SqlAlchemyAlbumRepository(AlbumRepository):
    def add(self, album):
        db_session.add(album)

    def remove(self, guid):
        db_session.query(Album).filter_by(guid=guid).delete()

    def get(self, guid):
        return db_session.query(Album).filter_by(guid=guid).first()

    def find(self):
        return db_session.query(Album).all()
