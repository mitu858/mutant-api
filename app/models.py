from . import db

class DNA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.String, unique=True, nullable=False)
    is_mutant = db.Column(db.Boolean, nullable=False)
