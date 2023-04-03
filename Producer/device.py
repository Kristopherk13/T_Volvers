
import random
import asyncio
import time

#Identificacion del dispositivo
idDevice = "2311"

#rango de datos de medición
min_range = 13
max_range = 1000
report = []

# creacion de tiempo  timestamp
def timestamp1():
    x = time.time()
    return x

def measure(min_range, max_range):
    return round(random.uniform(min_range, max_range), 2)

# generacion para la creacion de report
def data_report():
    #while True:
    data = measure(min_range, max_range)
    timestamp = timestamp1()
    report = {"id_dispositivo": str(idDevice),"timestamp": str(timestamp), "kWh": data}
    #await asyncio.sleep(1)
    print("\n",report)
    return report
    

# asyncio.run(data_report())
#report = data_report(223)
