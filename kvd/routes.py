from flask.blueprints import Blueprint
from flask import request

import json

from kvd.app import db
from kvd.upload import Upload

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    if request.headers.get('Content-Type') == 'application/json':
        return Upload.list_all()

    return 'Hello, World!'


@routes.route('/<string:key>', methods=['GET', 'POST', 'DELETE'])
def handle_upload(key: str):
    if request.method == 'POST':
        Upload(key, request.data, request.content_type).update()

    if request.method == 'DELETE':
        Upload.delete(key)

    upload = Upload.get(key)
    if upload is None:
        return 'Not found', 404

    return upload.data

@routes.route('/<string:key>/metadata')
def handle_metadata(key: str):
    upload = Upload.get(key)
    if upload is None:
        return 'Not found', 404

    return upload.meta()

