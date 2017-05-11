from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(11), unique=True)
    d_o_b = db.Column(db.String(120))
    gender = db.Column(db.String(10))
    profile_pic_path = db.Column(db.String(200))
 
# class Student(User):
#   	matric_no = db.Column(db.String(13), unique=True)
#   	pw_hash = db.Column(db.String(80))
#   	hostel_address = db.Column(db.String(80))
#   	interests = db.Column(db.Text)

#     # def __repr__(self):
#     #     return '<User %r>' % self.matric_no

# class Leturer(User):
#   	room_no = db.Column(db.String(8))
#   	specialization = db.Column(db.String(80))
#   	degree = db.Column(db.String(80))

#   	def __repr__(self):
#   		return '<User %r>' % self.username

