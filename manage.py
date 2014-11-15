from flask.ext.script import Manager
from enkindle import create_app


app = create_app()
manager = Manager(app)


if __name__ == "__main__":
    app.debug = True
    manager.run()
