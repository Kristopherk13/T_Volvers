from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import  engine, get_db
from functions import get_all_measure , get_measure_by_id_dispositivo, put_measure_by_id,       post_measure, delete_measure
from models import Measure

from fastapi.encoders import jsonable_encoder

Measure.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/measure/")
def read_allitems(db: Session = Depends(get_db)):
    return get_all_measure(db)

@app.get("/measure/{id_dispositivo}/")
def read_item(id_dispositivo: str, db: Session = Depends(get_db)):
    return get_measure_by_id_dispositivo(db,id_dispositivo)

@app.put("/measure/{id}/")
def update_item(id: int, id_dispositivo: str, timestamp: str, kWh : float, db: Session = Depends(get_db)):
    return put_measure_by_id(db,id,id_dispositivo,timestamp,kWh)


@app.post("/measure/{id_dispositivo}/")
def create_item(id_dispositivo: str, timestamp: str, kWh : float, db: Session = Depends(get_db)):
    return post_measure(db,id_dispositivo, timestamp, kWh)


@app.delete("/measure/{id}/")
def delete_item(id: int, db: Session = Depends(get_db)):
    return delete_measure(db,id)

