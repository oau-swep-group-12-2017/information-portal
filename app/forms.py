# from flask_wtf import Form
from wtforms import Form, SubmitField, HiddenField, BooleanField, TextAreaField, DateField, RadioField, StringField, SelectField, FileField, PasswordField, validators
from wtforms.validators import DataRequired

class RegistrationForm(Form):
    username = StringField('User Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    is_what = SelectField('Lecturer / Student',
                        [validators.DataRequired()],
                        choices=[('1', 'student'), ('2', 'lecturer')])
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])



class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    # remember_me = BooleanField('remember_me', default=False)

class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Message', validators=[DataRequired()])
    author = StringField('Author')

class ProfileForm(Form):
    username = StringField('User Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    first_name = StringField('First Name', [validators.Length(min=4, max=25)])
    last_name = StringField('Last Name', [validators.Length(min=4, max=25)])
    phone_number = StringField('Phone Number', [validators.Length(min=11, max=13)])
    # d_o_b = DateField('Date Of Birth', format="%m/%d/%Y")
    d_o_b = StringField('Date Of Birth')
    gender = RadioField('Label', choices=[('female','female'),('male','male')])
    # profile_pic_path = StringField('Profile Picture', [validators.Length(min=4, max=80)])
    matric_no = StringField('Matric Number', [validators.Length(min=13, max=13)])
    hostel_address = StringField('Hostel Address', [validators.Length(min=4, max=80)])
    interests = StringField('Interests')
    option = StringField('Option', [validators.Length(min=4, max=40)])
    room_no = StringField('Room Number', [validators.Length(min=4, max=8)])
    specialization = StringField('Specialization', [validators.Length(min=4, max=80)])
    degree = StringField('Degree', [validators.Length(min=4, max=80)])
    profile_pic = FileField('Upload Picture')
    # profile_pic = FileField('Upload Picture', [validators.regexp(u'^[^/\\]\.jpg$')])
    # is_lecturer = StringField('User Name', [validators.Length(min=4, max=25)])
    # is_student = StringField('User Name', [validators.Length(min=4, max=25)])

class SearchForm(Form):
    search = StringField('search', [DataRequired()])
    submit = SubmitField('Search')