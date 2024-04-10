from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'aa91be99e853f0ab9e018fa5'
db = SQLAlchemy(app)

from market import routes
