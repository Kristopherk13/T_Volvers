import asyncio
import aioredis
import requests
import csv
import matplotlib.pyplot as plt
import os.path as path

# Crear la figura y los ejes
fig, ax = plt.subplots()
data_count = []


url = 'http://localhost:8000/measure/'


async def main():
    redis = aioredis.from_url("redis://localhost:6379/")
    
    header = ["Id_dispositivo","Timestamp","kWh"]
            
    file = open("measure.csv", "w", newline='')
    spamreader = csv.writer(file)
    spamreader.writerow(header)

    while True:
        
        result = await redis.hgetall("data")
        if result is not None:
            
            # result = str(result).replace("b'", "'")
            # result= dict(result)
            id_dispositivo =(str(result[b'id_dispositivo']).replace("b'", "'")).replace("'", "")
            timestamp =(str(result[b'timestamp']).replace("b'", "'")).replace("'", "")
            kWh =(str(result[b'kWh']).replace("b'", "'")).replace("'", "")
            kWh = float(kWh)
            myobj = {
                "timestamp" : timestamp,
                "kWh" : kWh
            }
            url_to_send = url + id_dispositivo + "/"
            x = requests.post(url_to_send, params= result)
            
            lista = [str(id_dispositivo),str(timestamp),str(kWh)]
            
            file = open("measure.csv", "a", newline='')
            spamreader = csv.writer(file)
            spamreader.writerow(lista)
            file.close()
            print(x.text)
            
            # Lectura de grafico
            # with open('measure.csv', "r") as archivo:
            #     next(archivo, None)
            #     for linea in archivo:
            #     # Remover salto de línea
            #         linea = linea.rstrip()
            #         # Ahora convertimos la línea a arreglo con split
            #         lista = linea.split(",")
                                     
            # table = []
            # for data in data_count:
            #     if data not in table:
            #         table.append(data)
                    
            # ax.bar(table, [3, 2, 1])
            # ax.set_xlabel("Medida de dispositivo kWh")
            # plt.show()
            
        await asyncio.sleep(1)
        # print(result)
    


if __name__ == "__main__":
    asyncio.run(main())



