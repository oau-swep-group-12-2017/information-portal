from app.models import User
from app import db

__searchable__ = ['first_name', 'last_name', 'room_no']

class Search:
	def __init__(self):
		self.users = User.query.all()
		self.all_username = []
		self.all_first_name = []
		self.all_last_name = []
		self.all_room_number = []
		self.result = []
		self.load_users_filed()

	def load_users_filed(self):
		for user in self.users:
			self.all_username.append(user.username)
			self.all_first_name.append(user.first_name)
			self.all_last_name.append(user.last_name)
			self.all_room_number.append(user.room_no)

	def search_user(self, query):
		if query in self.all_username:
			self.result.append(User.query.filter(User.username == query)[0])
		if query in self.all_first_name:
			self.result.append(User.query.filter(User.first_name == query)[0])
		if query in self.all_last_name:
			self.result.append(User.query.filter(User.last_name == query)[0])
		if query in self.all_room_number:
			self.result.append(User.query.filter(User.room_no == query)[0])
		return self.result

		# if query in self.all_username:
		# 	user_found = User.query.filter(User.username == query)[0]
		# 	if user_found not in self.result:
		# 		self.result.append()
		# if query in self.all_first_name:
		# 	user_found = User.query.filter(User.first_name == query)[0]
		# 	if user_found not in self.result:
		# 		self.result.append
		# if query in self.all_last_name:
		# 	user_found = User.query.filter(User.last_name == query)[0]
		# 	if user_found not in self.result:
		# 		self.result.append
		# if query in self.all_room_number:
		# 	user_found = User.query.filter(User.last_name == query)[0]
		# 	if user_found not in self.result:
		# 		self.result.append
		# return self.result

if __name__ == '__main__':
	t = Search()
	r = t.search_user(unicode('Fasoyin'))
	for x in r:
		print x.email