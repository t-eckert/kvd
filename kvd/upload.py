from kvd.app import db
from typing import Optional
from datetime import datetime


class Upload(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    data = db.Column(db.LargeBinary, nullable=False)
    content_type = db.Column(db.String(80), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)
    last_accessed = db.Column(db.DateTime, nullable=False)

    def __init__(self, name: str, blob: bytes, content_type: str):
        self.name = name
        self.data = blob
        self.content_type = content_type
        self.size = len(blob)

    def __repr__(self):
        return '<Upload %r>' % self.name

    def meta(self) -> dict:
        """Gets the metadata of the upload."""
        return {
            'name': self.name,
            'contentType': self.content_type,
            'size': self.size,
            'created': self.created,
            'lastUpdated': self.last_updated,
            'lastAccessed': self.last_accessed
        }

    def insert(self):
        """Inserts the upload into the database."""

        self.created = datetime.utcnow()
        self.last_updated = datetime.utcnow()
        self.last_accessed = datetime.utcnow()

        db.session.add(self)
        db.session.commit()

    def update(self):
        """Updates the upload in the database."""
        if Upload.get(self.name) is not None:
            Upload.delete(self.name)
        self.insert()

    @staticmethod
    def get(name: str) -> Optional['Upload']:
        """Gets the upload from the database."""
        return db.session.query(Upload).filter_by(name=name).first()

    @staticmethod
    def delete(name: str):
        """Deletes the upload from the database."""
        db.session.query(Upload).filter_by(name=name).delete()
        db.session.commit()

    @staticmethod
    def list_all() -> list[dict]:
        # This is inefficient because it loads the blobs from the db
        return [upload.meta() for upload in db.session.query(Upload).all()]


