from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Enum
from sqlalchemy.ext.hybrid import hybrid_property
from bcrypt import hashpw, gensalt
from flask_bcrypt import Bcrypt
from config import app

bcrypt = Bcrypt(app)
db = SQLAlchemy()

# Models go here!
class Athlete(db.Model, SerializerMixin):
    __tablename__ = 'athletes'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    primary_sport = db.Column(Enum('Run', 'Bike'), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    activities = db.relationship('Activity', backref='athlete')
    menus = db.relationship('Menu', backref='athlete')
    meals = association_proxy('menus', 'meal')

    @hybrid_property
    def password(self):
        return self._password_hash 

    @password.setter
    def password(self, password):
        salt = gensalt()
        self._password_hash = hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    serialize_rules = ('-created_at', '-updated_at', '-activities', '-menus')

class Activity(db.Model, SerializerMixin):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.id'))
    type = db.Column(Enum('Run', 'Bike'), nullable=False)
    distance = db.Column(db.Integer)
    time = db.Column(db.Integer)
    pace = db.Column(db.Integer)
    calories_burned = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-created_at', '-updated_at', '-athlete_id')

    def __repr__(self):
        return f'Athlete_ID: {self.athlete_id} | Type: {self.type} | Distance: {self.distance} | Time: {self.time} | Pace: {self.pace} | Calories_Burned: {self.calories_burned}'

class Meal(db.Model, SerializerMixin):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    calories = db.Column(db.Integer)
    fats = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    proteins = db.Column(db.Integer)
    recipe = db.Column(db.String)

    athletes = association_proxy('menus', 'athlete')
    menus = db.relationship('Menu', backref='meal')

    serialize_rules = ('-athletes', '-menus')

    def __repr__(self):
        return f'Name: {self.name} | Calories: {self.calories} | Fats: {self.fats} | Carbs: {self.carbs} | Proteins: {self.proteins} | Recipe: {self.recipe}'

class Menu(db.Model, SerializerMixin):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.id'), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'))

    serialize_rules = ('-meal_id', '-athlete_id')