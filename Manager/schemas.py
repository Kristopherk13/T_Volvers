from pydantic import BaseModel


class MeasureBase(BaseModel):
    
    id_dispositivo : str 
    timestamp : str
    kWh : float
    
    class Config:
        orm_mode = True
    