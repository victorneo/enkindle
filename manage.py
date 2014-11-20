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


@manager.command
def createsprint():
    pid = int(prompt(name='Project id to create sprint for').strip())
    p = Project.query.filter(Project.id==pid).first()
    if not p:
        return 'No project with id {0} found'.format(pid)

    points = float(prompt(name='Points for this sprint').strip())
    start_date = prompt(name='Start date: (dd-mm-yyyy)').strip()
    end_date = prompt(name='End date: (dd-mm-yyyy)').strip()
    sprint_count = Sprint.query.filter(Sprint.project_id==pid).count() or 0

    start_date = datetime.strptime(start_date, '%d-%m-%Y').date()
    end_date = datetime.strptime(end_date, '%d-%m-%Y').date()
    sprint = Sprint(number=sprint_count+1, points=points, start_date=start_date,
                    end_date=end_date)
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

    burn_date = prompt(name='Date: (dd-mm-yyyy)').strip()
    points = float(prompt(name='Points completed').strip())

    burn_date = datetime.strptime(burn_date, '%d-%m-%Y').date()
    burn = Burn(date=burn_date, points=points, sprint_id=s.id)
    db.session.add(burn)
    db.session.commit()
    print 'Burn created for Sprint {0} on {1} with {2} points'\
            .format(s.id, burn_date, points)


if __name__ == "__main__":
    app.debug = True
    manager.run()
