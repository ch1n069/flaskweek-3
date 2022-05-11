from datetime import datetime
from . import db
#MOdel for comments or reviews
#models for users 
# model for categories
#model for votes
# model for pitches



# users models  

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    pitches = db.relationship('Pitch',backref='author', lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', {self.image_file}')"


class Pitch(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"post('{self.title}', '{self.date_posted}')"

    


