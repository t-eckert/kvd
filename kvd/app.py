from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kvd.db'

db.init_app(app)
CORS(app)

from kvd.upload import Upload # noqa

with app.app_context():
    db.create_all()

from kvd.routes import routes

app.register_blueprint(routes)

