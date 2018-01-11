from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# application is a Flask instance
application = Flask(__name__)
application.config.from_object(Config)
# db takes application instance to instantiate
db = SQLAlchemy(application)
migrate = Migrate(application, db)
# login manager
login = LoginManager(application)
login.login_view = 'login'

from app import routes, models
