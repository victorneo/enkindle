from .core import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sprints = db.relationship('Sprint', backref='project')


class Sprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    burns = db.relationship('Burn', backref='sprint')


class Burn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    points = db.Column(db.Float, nullable=False)
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprint.id'))
