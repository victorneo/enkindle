from datetime import datetime
from flask.ext.script import Manager, prompt
from enkindle import create_app


app = create_app()
manager = Manager(app)


from sqlalchemy import desc
from enkindle.core import db
from enkindle.models import Project, Sprint, Burn


@manager.command
def createproject():
    name = prompt(name='Project name').strip()
    p = Project(name=name)
    db.session.add(p)
    db.session.commit()
    print('Project id: {0}'.format(p.id))


@manager.command
def listprojects():
    print('Projects:')
    for p in Project.query.all():
        print('\tID: {0}, Name: {1}'.format(p.id, p.name))


@manager.command
def createsprint():
    pid = int(prompt(name='Project id to create sprint for').strip())
    p = Project.query.filter(Project.id==pid).first()
    if not p:
        return 'No project with id {0} found'.format(pid)

    points = float(prompt(name='Points for this sprint').strip())
    days = int(prompt(name='Number of days for this sprint').strip())
    sprint_count = Sprint.query.filter(Sprint.project_id==pid).count() or 0

    sprint = Sprint(number=sprint_count+1, points=points, days=days)
    db.session.add(sprint)
    db.session.commit()

    print 'Sprint {0} created for project {1}'.format(sprint.id, p.id)


@manager.command
def createburn():
    pid = int(prompt(name='Project id to create burn for').strip())
    p = Project.query.filter(Project.id==pid).first()
    if not p:
        print 'No project with id {0} found'.format(pid)
        return

    s = Sprint.query.order_by(desc(Sprint.number)).first()
    print "Creating burn for Sprint {0}".format(s.number)

    day = (Burn.query.filter(Burn.sprint_id==s.id).count() or 0) + 1
    points = float(prompt(name='Points completed').strip())

    burn = Burn(day=day, points=points, sprint_id=s.id)
    db.session.add(burn)
    db.session.commit()
    print 'Burn created for Sprint {0} with {1} points'\
            .format(s.id, points)


if __name__ == "__main__":
    app.debug = True
    manager.run()
