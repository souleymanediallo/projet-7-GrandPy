import random

from app.parser import Parser
from app.googlemaps import GoogleMaps
from app.wikipedia import Wikipedia
from app.grandpy import reponseListe


def app_grandpy(question):
    """
    The main implementation of all the application logic
    Create the parser for the questions asked analyzer
    Using the API Google maps
    Using the API Wikipedia
    """
    parser = Parser(question)
    question = parser.clean()
    gmaps = GoogleMaps()
    result_address = gmaps.search(question)
    wikip = Wikipedia()
    pages = wikip.search_for_pages(result_address["lat"],
                                   result_address["lng"])
    result_article, result_url = wikip.search_for_page_content(
        pages[0]["pageid"]
    )
    return {
        "parser": question,
        "grandpy": random.choice(reponseListe),
        "gmaps": result_address,
        "wikip": result_article,
        "wikip_url": result_url}
