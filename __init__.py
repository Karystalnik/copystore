import os
from config import DevelopmentConfig
from flask import Flask
from .database import db

def create_app():
	app = Flask(__name__)
	app.config.from_object(DevelopmentConfig)

	db.init_app(db, app)
	with app.test_request_context():
		db.create_all()

	import app.publickviews.controllers as publickviews
	app.register_blueprint(publickviews)

	return app

print(db)