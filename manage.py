from datetime import datetime
from flask.ext.script import Manager, prompt
from enkindle import create_app


app = create_app()
manager = Manager(app)


from enkindle.core import db
from enkindle.models import Project, Milestone, Sprint, Burn


@manager.command
def createproject():
    name = prompt(name='Project name:').strip()
    p = Project(name=name)
    db.session.add(p)
    db.session.commit()
    print('Project id: {0}'.format(p.id))


@manager.command
def listprojects():
    print('Project ids:')
    for p in Project.query.all():
        print(p.id)


if __name__ == "__main__":
    app.debug = True
    manager.run()
