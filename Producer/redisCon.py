import asyncio
import aioredis
from device import data_report 


async def main():
    
    redis = aioredis.from_url("redis://localhost:6379/")
    #await redis.hset("hash", mapping={"key1": "value1", "key2": "value2", "key3": 1456325})
    while True:
        await redis.hset("data", mapping=data_report())
        await asyncio.sleep(1)
    

if __name__ == "__main__":
    asyncio.run(main())
