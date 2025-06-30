import httpx
import asyncio
from selectolax.parser import HTMLParser
import time
import requests
from bs4 import BeautifulSoup
import time


urls = [
    # add your URLs here
]
    
# httpx + selectolax (async)
async def fetch(url, client):
    response = await client.get(url)
    tree = HTMLParser(response.text)
    title_node = tree.css_first("title")
    title = title_node.text() if title_node else "No title"
    print(f"{url}: {title}")

async def main():
    async with httpx.AsyncClient() as client:
        tasks = list(map(lambda x: fetch(x, client),urls))
        await asyncio.gather(*tasks)
start = time.time()
asyncio.run(main())
end = time.time()
print(f"Total time (httpx + selectolax async): {end - start:.2f} seconds")

# requests + BeautifulSoup
start = time.time()
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title"
    print(f"{url}: {title}")
end = time.time()
print(f"Total time (requests + BeautifulSoup): {end - start:.2f} seconds")

