def load_user(id):
    return User.query.get(int(id))