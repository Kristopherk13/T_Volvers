from sqlalchemy import  Column, Integer, String, Float , Identity
from database import Base


class Measure(Base):
    __tablename__ = "measure"
    id = Column(Integer, Identity(start=0, cycle=True), primary_key=True)
    id_dispositivo = Column(String)
    timestamp = Column(String)
    kWh = Column(Float)
    