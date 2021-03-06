from app_init import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    hash = db.Column(db.String(20), nullable=False)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    def __init__(self, email, hash_value, longitude, latitude):
        self.email = email
        self.hash = hash_value
        self.longitude = longitude
        self.latitude = latitude

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator = db.Column(db.Integer)#, db.ForeignKey('user.id'))
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    date = db.Column(db.String(40), nullable=False)
    time = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(30), nullable=True)
    profit = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    taken = db.Column(db.Integer, nullable=False)

    def __init__(self, creator, name, descripiton, addres, date, time, phone, profit, latitude, longitude):
        self.creator = creator
        self.name = name
        self.description = descripiton
        self.address = addres
        self.date = date
        self.time = time
        self.phone = phone
        self.profit = profit
        self.latitude = latitude
        self.longitude = longitude
        self.taken = False



