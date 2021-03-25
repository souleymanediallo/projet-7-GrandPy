import random

from app.parser import Parser
from app.googlemaps import GoogleMaps
from app.wikipedia import Wikipedia
from app.grandpy import *


def app_grandpy(question):
    parser = Parser(question)
    question = parser.clean()
    gmaps = GoogleMaps()
    result_address = gmaps.search(question)
    wikip = Wikipedia()
    pages = wikip.search_for_pages(result_address["lat"], result_address["lng"])
    result_article, result_url = wikip.search_for_page_content(pages[0]["pageid"])
    return {
        "grandpy": random.choice(reponseListe),
        "parser": question,
        "gmaps": result_address,
        "wikip": result_article,
        "wikip_url": result_url,
    }


