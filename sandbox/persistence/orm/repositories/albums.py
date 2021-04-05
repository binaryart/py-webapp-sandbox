from sandbox.domain.repositories.albums import AlbumRepository
from sandbox.domain.repositories.errors import RecordNotFoundException
from sandbox.persistence.orm.database import db_session
from sandbox.persistence.orm.models import Album


class SqlAlchemyAlbumRepository(AlbumRepository):
    def add(self, album):
        db_session.add(album)
        db_session.commit()

    def remove(self, id):
        album = self.get(id)
        if album:
            db_session.delete(album)
        else:
            raise RecordNotFoundException()

    def get(self, id):
        return db_session.query(Album).filter_by(id=id).first()

    def find(self):
        return db_session.query(Album).all()
