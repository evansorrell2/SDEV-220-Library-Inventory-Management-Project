#configure Flask and database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create Flask application
app = Flask(__name__)

#configure database
#specify database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
#turn off Flask-SQLAlchemy's track modifications to increase performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize database
db = SQLAlchemy(app)

from . import models, routes