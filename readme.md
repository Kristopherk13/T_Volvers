Diagrama de arquitectura se encuentra en formato .png
    .\Diagrama de arquitectura.png

Archivo .csv se crea en el directorio consumer para guardar las mediciones.
    .\Consumer\measure.csv

Los directorios se encuentran organizados de la siguiente manera:
    Consumer
        Microservicio que consulta los eventos en el redis.
    Consumer_event
        Microservicio que consulta los eventos de diferente manera, detecta overflow cada 50 mediciones.
    manager
        Se encuentra alojado el FASTAPI el cual contiene el CRUD para la administración de las mediciones.
    Produces
        Se encuentra alojado el dispositivo que genera mediciones aleatorias y las reporta al redis.

Guia para ejecucion de codigo:

Activar entorno virtual de \manager
    .\venv-manager\Scripts\activate

Activar entorno virtual de \Producer
    .\venv\Scripts\activate

Activar entorno virtual de \Consumer
    .\venv\Scripts\activate

Activar entorno virtual de \Consumer_event
    .\venv\Scripts\activate

correr servidor post-db (Base de datos) 
    docker run --name postgres-db -p 5432:5432 -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=device -e POSTGRES_USER=admin -d postgres
    
    docker start postgres-db

Correr servidor Fastapi 
    uvicorn main:app --reload 

Correr servicio redis. 
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest

Correr producer en directorio
    .\Prueba T_evolvers\Producer\python redisCon.py

Correr Consumer en directorio
    .\Prueba T_evolvers\Consumer\python consumer.py

Correr Consumer_event en directorio
    .\Prueba T_evolvers\Consumer\python Consumer_event.py

Los micro servicios estaran corriendo correctamente.

 


