from .core import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sprints = db.relationship('Sprint', backref='project')


class Sprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Float, nullable=False)
    days = db.Column(db.Integer, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    burns = db.relationship('Burn', backref='sprint')


class Burn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Float, nullable=False)
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprint.id'))
