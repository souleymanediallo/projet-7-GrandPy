from config import SECRET_KEY_API_GOOGLE
import googlemaps


class GoogleMaps:
    def __init__(self):
        self.gmaps = googlemaps.Client(key=SECRET_KEY_API_GOOGLE)

    def search(self, sentence):
        results = self.gmaps.geocode(sentence)
        if results:
            result = results[0]
            final_result = {
                "address": result["formatted_address"],
                "lat": result["geometry"]["location"]["lat"],
                "lng": result["geometry"]["location"]["lng"]
            }
            return final_result
        return {"address": None, "lat": None, "lng": None}
