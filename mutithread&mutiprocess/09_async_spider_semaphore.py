import asyncio
import aiohttp
import time

semaphore = asyncio.Semaphore(10)


async def async_crew(url):
    async with semaphore:
        print("craw url:", url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                # await asyncio.sleep(5)
                print(f"craw url:{url},{len(result)}")


urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50 + 1)
]

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_crew(url))
    for url in urls]

start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("cost:", end - start, "seconds")