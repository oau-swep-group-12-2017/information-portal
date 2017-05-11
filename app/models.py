from app import db, app
# import bcrypt


# import sys
# if sys.version_info >= (3, 0):
#     enable_search = False
# else:
#     enable_search = True
# import flask_whooshalchemy as whooshalchemy


class User(db.Model):
	__tablename__ = 'user'
	__table_args__ = (
        dict(
            sqlite_autoincrement=True))
	__searchable__ = ['first_name', 'last_name', 'room_no']

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(80), nullable=False)
	#: The hashed password
	password = db.Column(db.String(128), nullable=False)
	first_name = db.Column(db.String(30), nullable=True)
	last_name = db.Column(db.String(30), nullable=True)
	phone_number = db.Column(db.String(11))
	d_o_b = db.Column(db.String(120))
	gender = db.Column(db.String(10))
	profile_pic = db.Column(db.String(200))
	
	# student info
	matric_no = db.Column(db.String(13))
	option = db.Column(db.String(40))
	hostel_address = db.Column(db.String(80))
	interests = db.Column(db.Text)

	# lecturer info
	room_no = db.Column(db.String(8))
	specialization = db.Column(db.String(80))
	degree = db.Column(db.String(80))

	# role
	is_admin = db.Column(db.Boolean(), default=False)
	is_what = db.Column(db.String(10))

	#post
	#posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __init__(self, username, email, password=None, **kwargs):
		"""Create instance."""
		db.Model.__init__(self, username=username, email=email, password=password, **kwargs)
		# if password:
		# 	self.set_password(password)
		# else:
		# 	self.password = None

	# def set_password(self, password):
	# 	"""Set password."""
	# 	self.password = bcrypt.generate_password_hash(password)

	# def check_password(self, value):
	# 	"""Check password."""
	# 	return bcrypt.check_password_hash(self.password, value)

	@property
	def full_name(self):
		"""Full user name."""
		return '{0} {1}'.format(self.first_name, self.last_name)

	def __repr__(self):
		"""Represent instance as a unique string."""
		return '<User({username!r})>'.format(username=self.username)



class Post(db.Model):
	__searchable__ = ['body']

	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(140))
	body = db.Column(db.String(140))
	author = db.Column(db.String(50))
	timestamp = db.Column(db.DateTime)

	def __repr__(self):
		return '<Post %r>' % (self.body)


# class Student(User):
#   	matric_no = db.Column(db.String(13), unique=True)
#   	hostel_address = db.Column(db.String(80))
#   	interests = db.Column(db.Text)

#   	def __init__(self, username=username, email=email, password=password, **kwargs):
#   		db.Model.__init__(self, username=username, email=email, password=password, **kwargs)
#   		super.__init__()
#   	def __repr__(self):
#   		return '<User %r>' % self.matric_no

# class Leturer(User):
# 	room_no = db.Column(db.String(8))
# 	specialization = db.Column(db.String(80))
# 	degree = db.Column(db.String(80))

# 	def __init__(self, username=username, email=email, password=password, **kwargs):
# 		super.__init__(Student, self, username=username, email=email, password=password, **kwargs)

# 	def __repr__(self):
#   		return '<User %r>' % self.username


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password = db.Column(db.String(120), index=True, unique=True)

#     def __repr__(self):
#         return '<User %r>' % (self.nickname)
# if enable_search:
#whooshalchemy.whoosh_index(app, User)