from app import app, db
from app.forms import RegistrationForm, LoginForm, ProfileForm, PostForm, SearchForm
from app.models import User, Post
from flask import flash, g, request, render_template, redirect, url_for, session
# from flask_login import login_user, logout_user, current_user, login_required
from flask.ext.login import login_required, login_user, logout_user
from config import MAX_SEARCH_RESULTS
from search import Search
# from app.models import User



# @app.before_request
# def before_request():
#     g.search_form = SearchForm()

# @app.route('/search', methods=['POST'])
# # @login_required
# def search():
#     search_form = SearchForm()
#     # if not g.search_form.validate_on_submit():
#     if not True:
#         return redirect(url_for('index'))
#     print(g.search_form.data)
#     return redirect(url_for('search_results', query=g.search_form.search.data))

@app.route('/search_results/<query>')
#@login_required
def search_results(query):
    results = []
    query_strings = query.split(' ')
    print 'query_stringgs: ', query_strings
    for string in query_strings:
        s = Search()
        results += s.search_user(string)
    print 'results: ', results
    return render_template('search_results.html',
                           query=query,
                           results=results)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    search_form = SearchForm()
    if request.method == 'GET':
        posts = db.session.query(Post).order_by(Post.id)
        return render_template('home.html',
        					   title='Home',
                               posts=posts,
                               form=search_form)
    elif request.method == 'POST':
        print('got here: ')
        # print('data', search_form.search.data)
        print('data', request.form['search'])
        return redirect(url_for('search_results', query=request.form['search']))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = load_user(form.username.data)
        if valid_credentials(user, form.password.data):
            session['username'] = form.username.data
            return redirect(url_for('profile', username=form.username.data))
            # return redirect(request.args.get("next"))
        # else:
        #     return abort(401)
        else:
             return redirect(url_for('login', username=form.username.data))
    return render_template('login.html',
                            title='Login', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data,
                     password=form.password.data, is_what=form.is_what.data)
        print(form.username.data, form.email.data,
              form.password.data)
        db.session.add(user)
        db.session.commit()
        try:
            session['username'] = form.username.data
        except KeyError:
            pass
        #             form.password.data)
        # db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('edit', username=user.username))
    return render_template('register.html', form=form, title='Register')


# @app.route('/profile/<username>', methods=['GET', 'POST'])
# # @login_required
# def profile(username):
#     form = ProfileForm(request.form)
#     post_form = PostForm(request.form)
#     if request.method == 'GET':
#         user = load_user(username)
#         return render_template('profile.html',
#                                 form=form, user=user,
#                                 post_form=post_form,
#                                 title='Profile')
#     elif request.method == 'POST':
#         # update notice board
#         # print(request.form['author'])
#         # new_author = HiddenField(request.form['author'])
#         # new_post_form = PostForm(author=new_author)
#         print('its this type: ', type(post_form.title.data))
#         post_form.author.data = request.form['author']
#         post = Post(title=post_form.title.data, body=post_form.body.data,
#             author=post_form.author.data)
#         db.session.add(post)
#         db.session.commit()
#         return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
# @login_required
def profile(username=None):
    form = ProfileForm(request.form)
    post_form = PostForm(request.form)
    if request.method == 'GET':
        if not username:
            try:
                username = session['username']
            except KeyError:
                pass
        user = load_user(username)
        return render_template('profile.html',
                                form=form, user=user,
                                post_form=post_form,
                                title='Profile')
    elif request.method == 'POST':
        # update notice board
        # print(request.form['author'])
        # new_author = HiddenField(request.form['author'])
        # new_post_form = PostForm(author=new_author)
        print('its this type: ', type(post_form.title.data))
        post_form.author.data = request.form['author']
        post = Post(title=post_form.title.data, body=post_form.body.data,
            author=post_form.author.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))


# @app.route('/edit/<username>', methods=['GET', 'POST'])
# @login_required
# def edit(username):
#     form = ProfileForm(request.form)
#     user = load_user(username)

#     if request.method == 'GET':
#         print('username: ', username)
#         print(user)
#         return render_template('edit_profile.html',
#                                 form=form, user=user, title='Profile')
#     elif request.method == 'POST':
#         fields = ['first_name', 'last_name', 
#                 'phone_number', 'd_o_b',
#                 'gender', 'profile_pic']
        
#         lecturer_fields = ['room_no',
#                 'specialization', 'degree'
#                 ]

#         student_fields = ['matric_no', 'option', 'hostel_address', 
#                         'interests']
#         if user.is_what == '1':
#             print('assumed student')
#             fields += student_fields
#         elif user.is_what == '2':
#             print('assumed lecturer')
#             fields += lecturer_fields
#         data_update = {}
#         print('form: ', form)
#         # for field in fields:
#         #     try:
#         #         if data[field]:
#         #             if data[field] != '' or data[field] is not None:
#         #                 data[field] = form[field].data
#         #     except KeyError:
#         #         print('KeyError: ', field)
#         #         pass

#         for field in fields:
#             try:
#                 data_update[field] = form[field].data
#             except KeyError:
#                 print('KeyError: ', field)
#                 pass

#         print(data_update)

#         # update data in db
#         db.session.query(User).filter_by(username=User.username).update(data_update)
#         db.session.commit()
#         return redirect(url_for('profile', username=user.username))

@app.route('/edit', methods=['GET', 'POST'])
# @login_required
def edit():
    form = ProfileForm(request.form)
    username = session['username']
    user = load_user(username)

    if request.method == 'GET':
        print('username: ', username)
        print(user)
        return render_template('edit_profile.html',
                                form=form, user=user, title='Profile')
    elif request.method == 'POST':
        fields = ['first_name', 'last_name', 
                'phone_number', 'd_o_b',
                'gender', 'profile_pic']
        
        lecturer_fields = ['room_no',
                'specialization', 'degree'
                ]

        student_fields = ['matric_no', 'option', 'hostel_address', 
                        'interests']
        if user.is_what == '1':
            print('assumed student')
            fields += student_fields
        elif user.is_what == '2':
            print('assumed lecturer')
            fields += lecturer_fields
        data_update = {}
        print('form: ', form)
        # for field in fields:
        #     try:
        #         if data[field]:
        #             if data[field] != '' or data[field] is not None:
        #                 data[field] = form[field].data
        #     except KeyError:
        #         print('KeyError: ', field)
        #         pass

        for field in fields:
            try:
                data_update[field] = form[field].data
            except KeyError:
                print('KeyError: ', field)
                pass

        new_data_update = {k:data_update[k] for k in data_update if data_update[k] != ''}

        print(new_data_update)

        # update data in db
        db.session.query(User).filter_by(username=User.username).update(new_data_update)
        db.session.commit()
        return redirect(url_for('profile', username=user.username))

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


def load_user(username):
    return User.query.filter(User.username == username)[0]

def valid_credentials(user_obj, password):
    if user_obj.password == password:
        return True
    else:
        return False