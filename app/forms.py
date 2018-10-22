from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Department, Manufacturer

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    #submit = SubmitField('Sign In')


def department_query():
	return Department.query

class LocationForm(FlaskForm):
    name = StringField('Location name', validators=[DataRequired()])
    department_list = QuerySelectField(query_factory=department_query, allow_blank=False, get_label='name')
    #submit = SubmitField('Sign In')


class DepartmentForm(FlaskForm):
    name = StringField('Department Name', validators=[DataRequired()])


    def validate_name(self, name):
        department = Department.query.filter_by(name=name.data).first()
        if department is not None:
            raise ValidationError('Department alreadey exists. Please use another name.')


class ManufacturerForm(FlaskForm):
    name = StringField('Manufacturer Name', validators=[DataRequired()])


    def validate_name(self, name):
        manufacturer = Manufacturer.query.filter_by(name=name.data).first()
        if manufacturer is not None:
            raise ValidationError('Manufacturer alreadey exists. Please use another name.')