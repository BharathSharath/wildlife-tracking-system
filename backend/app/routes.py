from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, utils

router = APIRouter()

@router.post("/species/", response_model=schemas.Species)
def create_species(species: schemas.SpeciesCreate, db: Session = Depends(utils.get_db)):
    db_species = models.Species(**species.dict())
    db.add(db_species)
    db.commit()
    db.refresh(db_species)
    return db_species

@router.post("/animals/", response_model=schemas.Animal)
def create_animal(animal: schemas.AnimalCreate, db: Session = Depends(utils.get_db)):
    db_animal = models.Animal(**animal.dict())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

@router.post("/tracking/", response_model=schemas.Tracking)
def create_tracking(tracking: schemas.TrackingCreate, db: Session = Depends(utils.get_db)):
    db_tracking = models.Tracking(**tracking.dict())
    db.add(db_tracking)
    db.commit()
    db.refresh(db_tracking)
    return db_tracking

@router.post("/health_records/", response_model=schemas.HealthRecord)
def create_health_record(record: schemas.HealthRecordCreate, db: Session = Depends(utils.get_db)):
    db_record = models.HealthRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
