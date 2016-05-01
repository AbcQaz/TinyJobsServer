from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.sqlalchemy import SQLAlchemy


SQLALCHEMY_TRACK_MODIFICATIONS = True
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://mic:mic@localhost/TinyJobs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.debug = True
api = Api(app)
db = SQLAlchemy(app)