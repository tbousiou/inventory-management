from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))


	def __repr__(self):
		return '<User {}>'.format(self.username)


class Asset(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	model = db.Column(db.String(64), index=True, unique=False)
	
	manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

	def __repr__(self):
		return '<Asset {}>'.format(self.model)


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)

	assets = db.relationship('Asset', backref="category")

	def __repr__(self):
		return '<Category {}>'.format(self.name)


class Manufacturer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	
	assets = db.relationship('Asset', backref="manufacturer")

	def __repr__(self):
		return '<Manufacturer {}>'.format(self.name)


class Location(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))

	department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
	
	assets = db.relationship('Asset', backref="location")

	def __repr__(self):
		return '<Location {}>'.format(self.name)

class Department(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)


	locations = db.relationship('Location', backref="department")

	def __repr__(self):
		return '<Department {}>'.format(self.name)