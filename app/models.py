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
	manufacturer = db.Column(db.String(64), index=True, unique=True)
	location = db.Column(db.String(64), index=True, unique=True)

	def __repr__(self):
		return '<Asset {}>'.format(self.model)


class Location(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)

	def __repr__(self):
		return '<Location {}>'.format(self.name)