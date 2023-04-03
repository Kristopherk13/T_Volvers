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

 


