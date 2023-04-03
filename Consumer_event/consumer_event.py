import asyncio
import aioredis
import requests



url = 'http://localhost:8000/measure/'


async def main():
    count = 0
    redis = aioredis.from_url("redis://localhost:6379/")
    while True:
        
        result = await redis.hgetall("data")
        if result is not None:
            count += 1
            print("count =" , count)
            
            if count >= 50:
                print("¡¡¡OVERFLOW!!!")
                count = 0

            
        await asyncio.sleep(1)
        print(result)


if __name__ == "__main__":
    asyncio.run(main())



