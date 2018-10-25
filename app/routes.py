from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, DepartmentForm, LocationForm, ManufacturerForm, CategoryForm
from app.models import Asset, Location, Category, Manufacturer, Department, User

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Teo'}
	assets = [
		{
			'model': 'Macbook Pro',
			'manufacturer': 'Apple',
			'location': 'Lab 15'
		},
		{
			'model': 'MX 345',
			'manufacturer': 'Dell',
			'location': 'Lab 12'
		}
	]
	return render_template('index.html', title='Home', user=user, assets=assets)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



@app.route('/assets')
def assets():
	assets = Asset.query.all()
	return render_template('assets.html', title='Assets', assets=assets)


@app.route('/locations')
def locations():
	locations = Location.query.all()
	return render_template('locations.html', title='Locations', locations=locations)


@app.route('/locations/create', methods=['GET', 'POST'])
def create_location():
	form = LocationForm()
	form.department_id.choices = [(d.id, d.name) for d in Department.query.order_by('name')]
	if form.validate_on_submit():
		location = Location(name=form.name.data, department_id=form.department_id.data)
		db.session.add(location)
		db.session.commit()
		return redirect(url_for('locations'))
	return render_template('locations-create.html', title='Create Location', form=form)

@app.route('/departments')
def departments():
	departments = Department.query.all()
	return render_template('departments.html', title='Departments', departments=departments)

@app.route('/departments/create', methods=['GET', 'POST'])
def create_department():
	form = DepartmentForm()
	if form.validate_on_submit():
		department = Department(name=form.name.data.strip())
		db.session.add(department)
		db.session.commit()
		return redirect(url_for('departments'))
	return render_template('departments-create.html', title='Create Department', form=form)


@app.route('/categories')
def categories():
	categories = Category.query.all()
	return render_template('categories.html', title='Categories', categories=categories)

@app.route('/categories/create', methods=['GET', 'POST'])
def create_category():
	form = CategoryForm()
	#if form.validate_on_submit():
	#	manufacturer = Manufacturer(name=form.name.data.strip())
	#	db.session.add(manufacturer)
	#	db.session.commit()
	#	return redirect(url_for('manufacturers'))
	return render_template('categories-create.html', title='Create Manufacturer', form=form)

@app.route('/manufacturers')
def manufacturers():
	manufacturers = Manufacturer.query.all()
	return render_template('manufacturers.html', title='Manufacturers', manufacturers=manufacturers)

@app.route('/manufacturers/create', methods=['GET', 'POST'])
def create_manufacturer():
	form = ManufacturerForm()
	if form.validate_on_submit():
		manufacturer = Manufacturer(name=form.name.data.strip())
		db.session.add(manufacturer)
		db.session.commit()
		return redirect(url_for('manufacturers'))
	return render_template('manufacturers-create.html', title='Create Manufacturer', form=form)

@app.route('/users')
def users():
	users = User.query.all()
	return render_template('users.html', title='Users', users=users)
