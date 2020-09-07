from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class usernameForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Get Logs')

class addUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
    view = SubmitField('Update')
    compare = SubmitField('+')

class compareUserForm(FlaskForm):
    username1 = StringField('Username')
    username2 = StringField('Username')
    update = SubmitField('Update')
    remove1 = SubmitField('-')
    remove2 = SubmitField('-')