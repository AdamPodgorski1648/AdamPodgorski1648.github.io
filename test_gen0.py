import requests as req
from bs4 import BeautifulSoup

from duckduckgo_search import DDGS
import re
import os
import time
from mdutils.mdutils import MdUtils

names = ["python"]

for name in names:
    request = req.get(
        DDGS().text(name + " language wikipedia", max_results=1)[0]['href'])

    soup = BeautifulSoup(request.text, 'html.parser')

events = body.find_all("tr")


names_unfiltered = []
links = []

input("")

# events[0].find_all("td")
# events[0].find_all("td")[3].find("img")

for event in events:
    names_unfiltered.append(event.find_all("td")[4].get_text())
    links.append(event.find_all("td")[3].img["src"])

