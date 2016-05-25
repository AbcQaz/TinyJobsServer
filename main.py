from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import flask_restful
import types
from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from app_init import app, api, db
from database import Job, User
import pymssql

users = {'m@w': 'm'}

todos = {}
jobs = []

# ************************source: http://flask.pocoo.org/snippets/129/
def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

api.route = types.MethodType(api_route, api)
# *************************


@api.route('/putjob')
class PutJob(Resource):
    def post(self):
        # todos[todo_id] = {'data': request.form['data'], 'user': request.form['user']}
        # print(todos)
        # return {todo_id: todos[todo_id]}
        try:
            job = Job(User.query.filter_by(email=request.form['user']).first().id,
                      request.form['name'],
                      request.form['description'],
                      request.form['address'],
                      request.form['date'],
                      request.form['time'],
                      request.form['phone'],
                      request.form['profit'],
                      request.form['latitude'],
                      request.form['longitude'])
            db.session.add(job)
            db.session.commit()

            # dupa = tuples_to_json(Job.query.all()).data
            # print(dupa)

        except pymssql.IntegrityError as e:
            print(e)
            return {'response': 'Bad values'}

@api.route('/getmyjobs')
class GetMyJobs(Resource):
    def post(self):
        return tuples_to_json(Job.query.filter_by(taken=User.query.filter_by(email=request.form['user']).first().id).all)


@api.route('/takejob')
class TakeJob(Resource):
    def post(self):
        job = Job.query.filter_by(id=request.form['id']).first()
        job.taken = User.query.filter_by(email=request.form['user']).first().id
        db.commit();


@api.route('/login')
class Login(Resource):
    def post(self):
        params = {'email': request.form['email'],
                  'hash': request.form['hash']}
        try:
            user = User.query.filter_by(email=params['email'], hash=params['hash']).first()
            if user is not None:
                user.longitude = request.form['longitude']
                user.latitude = request.form['latitude']
                db.session.commit()
                return {'response': 'true', 'userID': user.id}
            if user is None:
                return {'response': 'false'}
            flask_restful.abort(400)
            #return {'response': 'false'}

        except Exception as e:
            print(e)

@api.route('/register')
class Register(Resource):
    def post(self):
        try:
            user = User(request.form['email'], request.form['hash'], request.form['longitude'], request.form['latitude'])
            db.session.add(user)
            db.session.commit()
            print 'User registered: ', user.email
            return {'response': 'User registered'}

        except pymssql.IntegrityError as e:
            print(e)
            return {'response': 'Username already exists'}


@api.route('/getjobs')
class GetJobs(Resource):
    def post(self):
        try:
            jobs = Job.query.filter_by(taken=0).all()
            return tuples_to_json(jobs)
        except Exception as e:
            print(e)

@api.route('/taken')
class Taken(Resource):
    def post(self):
        try:
            jobs = Job.query.filter_by(taken=request.form['id']).all()
            return tuples_to_json(jobs)
        except Exception as e:
            print(e)

@api.route('/ordered')
class Ordered(Resource):
    def post(self):
        try:
            id = request.form['id']
            jobs = Job.query.filter_by(creator=id).all()
            return tuples_to_json(jobs)
        except Exception as e:
            print(e)

# @api.route('getmyjobs')
# class GetMyJobs(Resource):
#     def post(self):
#         try:
#             jobs = Job.query.filter_by()

def tuples_to_json(tuples):
    if isinstance(tuples, list):
        tab = []
        for t in tuples:
            tab.append(row2dict(t))
        return jsonify(results=tab)
    c = list(tuples)
    return jsonify(results=row2dict(list(tuples)))


def row2dict(row):  # takes a SQLAlchemy tuple and converts it to dictionary
    d = {}
    for column in row.__table__.columns:
        d[column.name] = unicode(getattr(row, column.name))
        c = []
    return d

if __name__ == '__main__':
    app.run(host='0.0.0.0')
