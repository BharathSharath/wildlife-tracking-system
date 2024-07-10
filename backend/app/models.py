from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Species(Base):
    __tablename__ = 'species'
    species_id = Column(Integer, primary_key=True, autoincrement=True)
    common_name = Column(String(100))
    scientific_name = Column(String(100))
    conservation_status = Column(String(50))

class Animal(Base):
    __tablename__ = 'animals'
    animal_id = Column(Integer, primary_key=True, autoincrement=True)
    species_id = Column(Integer, ForeignKey('species.species_id'))
    name = Column(String(100))
    birth_date = Column(Date)
    gender = Column(String(1))
    species = relationship('Species')

class Tracking(Base):
    __tablename__ = 'tracking'
    tracking_id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey('animals.animal_id'))
    timestamp = Column(Date)
    latitude = Column(Float)
    longitude = Column(Float)
    animal = relationship('Animal')

class HealthRecord(Base):
    __tablename__ = 'health_records'
    record_id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey('animals.animal_id'))
    checkup_date = Column(Date)
    health_status = Column(String(100))
    notes = Column(String(255))
    animal = relationship('Animal')
