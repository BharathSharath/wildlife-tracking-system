from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class SpeciesBase(BaseModel):
    common_name: str
    scientific_name: str
    conservation_status: str

class SpeciesCreate(SpeciesBase):
    pass

class Species(SpeciesBase):
    species_id: int

    class Config:
        orm_mode = True

class AnimalBase(BaseModel):
    name: str
    birth_date: date
    gender: str

class AnimalCreate(AnimalBase):
    species_id: int

class Animal(AnimalBase):
    animal_id: int
    species: Species

    class Config:
        orm_mode = True

class TrackingBase(BaseModel):
    timestamp: date
    latitude: float
    longitude: float

class TrackingCreate(TrackingBase):
    animal_id: int

class Tracking(TrackingBase):
    tracking_id: int
    animal: Animal

    class Config:
        orm_mode = True

class HealthRecordBase(BaseModel):
    checkup_date: date
    health_status: str
    notes: Optional[str]

class HealthRecordCreate(HealthRecordBase):
    animal_id: int

class HealthRecord(HealthRecordBase):
    record_id: int
    animal: Animal

    class Config:
        orm_mode = True
