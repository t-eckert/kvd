from flask.blueprints import Blueprint
from flask import request

from kvd.app import db
from kvd.upload import Upload

routes = Blueprint('routes', __name__)


@routes.route('/<string:key>', methods=['GET', 'POST', 'DELETE'])
def index(key: str):

    if request.method == 'POST':
        db.session.add(Upload(key, request.data))
        db.session.commit()

    if request.method == 'DELETE':
        db.session.query(Upload).filter_by(name=key).delete()
        db.session.commit()

    upload = db.session.query(Upload).filter_by(name=key).first()

    if upload is None:
        return 'Not found', 404

    return upload.data
