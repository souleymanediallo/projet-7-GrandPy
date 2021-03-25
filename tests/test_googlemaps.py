import json
from app import googlemaps


def test_search_position(mykey):
    address = 'YYYY'
    latitude = 66.00
    longitude = 2.000
    results = [{
        "formatted_address": address,
        "geometry": {"location": {"lng": longitude, "lat": latitude}}
    }]

    class MyClient:
        def __init__(self, key):
            pass

        def geocode(self, sentence):
            return results

    mykey.setattr("googlemaps.Client", MyClient)
    gmaps = googlemaps.GoogleMaps()
    results = gmaps.search("Hello")
