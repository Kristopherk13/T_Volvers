from sqlalchemy.orm import Session
from fastapi import  HTTPException

from models import Measure
from schemas import MeasureBase


def get_all_measure(db: Session):
    return db.query(Measure).all()


def get_measure_by_id_dispositivo(db: Session, id_dispositivo: str):
    return db.query(Measure).filter(Measure.id_dispositivo == id_dispositivo).order_by(Measure.timestamp.desc()).first()

def put_measure_by_id(db: Session, id: int, id_dispositivo: str,timestamp : str,kWh : int):
    measure_update = {
        "id" : id, 
        "id_dispositivo" : id_dispositivo,
        "timestamp" :timestamp,
        "kWh": kWh
        }
    measure_to_edit = db.get(Measure, id)
    if not measure_to_edit:
        raise HTTPException(status_code=404, detail="Id not found")
    for key, value in measure_update.items():
        setattr(measure_to_edit, key, value)
    db.add(measure_to_edit)
    db.commit()
    db.refresh(measure_to_edit)
    return measure_to_edit


def post_measure(db: Session, id_dispositivo: str, timestamp: str, kWh : float):
    db_measure = Measure(id_dispositivo = id_dispositivo, timestamp= timestamp, kWh = kWh)
    db.add(db_measure)
    db.commit()
    db.refresh(db_measure)
    return db_measure

def delete_measure(db: Session,id: str):
    measure_to_delete = db.get(Measure, id)
    if not measure_to_delete:
        raise HTTPException(status_code=404, detail="Id not found")
    db.delete(measure_to_delete)
    db.commit()
    # db.refresh(measure_to_delete)
    