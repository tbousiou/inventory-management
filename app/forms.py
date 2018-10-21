from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Department

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    #submit = SubmitField('Sign In')


class LocationForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    #submit = SubmitField('Sign In')


class DepartmentForm(FlaskForm):
    name = StringField('Department Name', validators=[DataRequired()])


    def validate_name(self, name):
        department = Department.query.filter_by(name=name.data).first()
        if department is not None:
            raise ValidationError('Department alreadey exists. Please use another name.')