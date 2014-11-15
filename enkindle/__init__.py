from flask import Flask
from .core import assets, db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enkindle.db'

    db.init_app(app)
    assets.init_app(app)

    from .views import views
    app.register_blueprint(views)

    return app
