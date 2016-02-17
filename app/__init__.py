from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'hard to guess string'
	
	bootstrap.init_app(app)

	from main import main as main_blueprint  
	app.register_blueprint(main_blueprint)

	return app
