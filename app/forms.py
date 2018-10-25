from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Department, Manufacturer, Category

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    #submit = SubmitField('Sign In')


class AssetForm(FlaskForm):
    model = StringField('Username', validators=[DataRequired()])
    

    manufacturer_id = SelectField('Manufacter', coerce=int)
    location_id = SelectField('Location', coerce=int)
    category_id = SelectField('Category', coerce=int)




class LocationForm(FlaskForm):
    name = StringField('Location name', validators=[DataRequired()])
    department_id = SelectField('Department', coerce=int)
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

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired()])


    def validate_name(self, name):
        category = Category.query.filter_by(name=name.data).first()
        if category is not None:
            raise ValidationError('Category alreadey exists. Please use another name.')