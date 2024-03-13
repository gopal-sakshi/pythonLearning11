import aiohttp
import asyncio
from async_timeout import timeout as timeout23

async def download23(url, file_path):
    async with aiohttp.ClientSession() as session:
        async with timeout23(600):
            async with session.get(url) as response:
                with open(file_path, 'wb') as f_handle:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        print("writing chunk ===> ", chunk, "\n\n\n")
                        f_handle.write(chunk)
                return await response.release()

asyncio.run(download23("https://www.gutenberg.org/cache/epub/98/pg98.txt","08_others/download23.txt"))