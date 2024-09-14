import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    date = Column(Date, index=True)
    
    def to_dict(self):
        return {}
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    origin_planet = Column(Integer, ForeignKey("planet.id"))
    height = Column(String(250), nullable=False)
    mass = Column(Float, nullable=False)
    unit_heigth = Column(String(250), nullable=False)
    unit_mass = Column(String(250), nullable=False)

    def to_dict(self):
        return {}
    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    surface_water= Column(Integer, nullable=False)
    diameter= Column(Integer, nullable=False)

    def to_dict(self):
        return {}

class vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)

    def to_dict(self):
        return {}


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    year = Column(Date, index=True)
    duration = Column(Integer, nullable=False)
    director = Column(String(250), ForeignKey("director.id"))


    def to_dict(self):
        return {}
    
class Director(Base):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)

    def to_dict(self):
        return {}

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"))
    films = Column(Integer, ForeignKey("films.id"))
    character = Column(Integer, ForeignKey("character.id"))
    vehicles = Column(Integer, ForeignKey("vehicles.id"))
    planet = Column(Integer, ForeignKey("planet.id"))

    def to_dict(self):
        return {}



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('User.id'))
#     person = relationship(User)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
