from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'

db.init_app(app)

from kvd.upload import Upload

with app.app_context():
    db.create_all()

from kvd.routes import routes

app.register_blueprint(routes)

