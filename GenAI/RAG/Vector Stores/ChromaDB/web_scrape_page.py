import os
import requests
from bs4 import BeautifulSoup
import rich as r

parentDir = os.path.dirname(os.path.abspath(__file__))

listCurrentDir = os.listdir(parentDir)

if "html_pages" not in listCurrentDir:
    page = requests.get(url="https://realpython.com/python-gil/")
    content = BeautifulSoup(page.content, "lxml")
    os.mkdir(parentDir + "/html_pages")

    with open(parentDir + "/html_pages/python_gil.html", mode="w", encoding="utf-8") as f:
        f.write(str(content.prettify()))