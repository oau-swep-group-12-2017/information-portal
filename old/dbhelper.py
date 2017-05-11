# from models import Student, Lecturer
from models import User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_name = 'test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

if not os.path.exists(os.path.join(os.getcwd(), db_name)):
	db.create_all()



class StudentAPI(User):
	def get_student(self, matric_no):
		pass
		# student = Student.query.filter_by(matric_no=data['matric_no'])
		# return student
	def add_student(self, data):
		# new_student = Student(first_name=data['first_name'],
		# 					  last_name=data['last_name'],
		# 					  email=data['email'],
		# 					  phone_number=data[])
		new_student = User(**data)
		db.session.add(new_student)
		db.session.commit()

	def remove_student(self, data):
		pass
		# # student = Student.query.filter_by(matric_no=data['matric_no']).first()
		# db.session.delete(student)
		# print db.session.commit()

	def edit_student(self, data):
		pass
		# student = Student.query.filter_by(matric_no=data['matric_no']).first()
		# for field in data:
		# 	if data[field]:
		# 		student[field] = data[field]
		# 		db.session.commit()


# class LectureAPI(Lecturer):
# 	def __init__(self):
# 		pass

if __name__ == '__main__':
	test = StudentAPI()
	
	data = {
			'first_name': 'first_name',
		 	'last_name': 'last_name',
		    'email': 'test@gmail.com',
		 	'phone_number': '08033985678',
		 	'd_o_b': 'August 3',
		 	'gender': 'Male'
  			}
	
	print test.add_student(data)