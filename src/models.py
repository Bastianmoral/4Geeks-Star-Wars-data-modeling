import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(80), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(150), nullable=False)
    home _planet = Column(Integer, ForeignKey('Planet.id'))
    fav_char = Column(Integer, ForeignKey('Favorites.favorite_character'))
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(150), nullable=False)
    character_planet = Column(Integer, ForeignKey('Character.id'))
    population = Column(Integer)
    fav_planets = Column(Integer, ForeignKey('Favorites.favorite_planet'))
    user = relationship(User)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(150), nullable=False)
    vehicle_model = Column(String(150),nullable=False)
    vehicle_manofacturer = Column(String(150),nullable=False)
    vehicle_pilot = Column(String(150), ForeignKey('Character.id'))
    fav_vehicles = Column(Integer, ForeignKey('Favorites.favorite_vehicle'))
    user = relationship(User)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite_character  = Column(String(200), nullable=False)
    favorite_planet  = Column(String(200), nullable=False)
    favorite_vehicle  = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'))
    user_favorites = relationship(User)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')