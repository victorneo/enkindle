from .core import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    milestones = db.relationship('Milestone', backref='project')


class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    deadline = db.Column(db.Date, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    sprints = db.relationship('Sprint', backref='milestone')


class Sprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    milestone_id = db.Column(db.Integer, db.ForeignKey('milestone.id'))
    burns = db.relationship('Burn', backref='sprint')


class Burn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprint.id'))
