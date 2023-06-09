from flask import request, send_from_directory, Response
from flask.blueprints import Blueprint

from kvd.upload import Upload

routes = Blueprint('routes', __name__)


def serve_index():
    return send_from_directory('static', 'index.html')


@routes.route('/')
def serve_assets():
    return Upload.list_all()


@routes.route('/string:key>', methods=['GET', 'POST', 'DELETE'])
def handle_upload(key: str):
    if request.method == 'POST':
        Upload(key, request.data, request.content_type).update()

    if request.method == 'DELETE':
        Upload.delete(key)

    upload = Upload.get(key)
    if upload is None:
        return Response('Not found', 404)

    return  Response(upload.data, 200, {'Content-Type': upload.content_type})


@routes.route('/<string:key>/metadata')
def handle_metadata(key: str):
    upload = Upload.get(key)
    if upload is None:
        return Response('Not found', 404)

    return Response(upload.meta(), 200, {'Content-Type': 'application/json'})

