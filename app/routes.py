from flask import render_template
from app import app

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