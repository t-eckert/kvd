from kvd.app import db


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, name: str, blob: bytes):
        self.name = name
        self.data = blob

    def __repr__(self):
        return '<Upload %r>' % self.name
