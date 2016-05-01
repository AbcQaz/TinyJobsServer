from app_init import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    hash = db.Column(db.String(20), nullable=False)

    def __init__(self, email, hash_value):
        self.email = email
        self.hash = hash_value

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #creator = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    date = db.Column(db.String(40), nullable=False)
    time = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(30), nullable=True)
    profit = db.Column(db.String(20), nullable=False)

    def __init__(self, name, descripiton, addres, date, time, phone, profit):
        self.name = name
        self.description = descripiton
        self.address = addres
        self.date = date
        self.time = time
        self.phone = phone
        self.profit = profit


