import requests
from bs4 import BeautifulSoup
import time

urls = [ "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods",
         "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods",
         "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods",
         "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods",
         "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods",
         "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods",
         "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods",
         "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods",
         "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods",
         "https://www.pythonsnacks.com/p/python-watchdog-file-directory-updates",
         "https://www.pythonsnacks.com/p/comparing-3-data-viz-libraries", 
         "https://www.pythonsnacks.com/p/why-python-does-not-have-private-methods"]

start = time.time()

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title"
    print(f"{url}: {title}")
end = time.time()
print(f"Total time (requests + BeautifulSoup): {end - start:.2f} seconds")