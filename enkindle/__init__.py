from flask import Flask
from .core import assets, db


def create_app(config_file='config'):
    app = Flask(__name__)
    app.config.from_object(config_file)

    db.init_app(app)
    assets.init_app(app)

    from .views import views
    app.register_blueprint(views)

    return app
