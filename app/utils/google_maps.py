from config import *
import requests


class GoogleMaps:
    def __init__(self, position):
        self.key = SECRET_KEY_API_GOOGLE
        self.api_url = GOOGLE_API_URL
        self.position = position
        self.content = self.get_address()

    @property
    def latitude(self):
        if self.content is not None:
            return self.content.get("lat")

    @property
    def longitude(self):
        if self.content is not None:
            return self.content.get("lng")

    def get_address(self):
        parameters = {
            "address": self.position,
            "key": self.key,
        }
        response = requests.get(self.api_url, params=parameters)

        if response.status_code == 200:
            content = response.json()
            if content.get("status") == "OK":
                return content.get("results")[0].get("geometry").get("location")
            else:
                print("Google API error : status not OK")
        else:
            api_error = f"Google API error : {response.status_code}"
            print(api_error)

# TODO 1: CRÉER LE PARSER QUI VA TRAITER LA QUESTION DE L'UTILISATEUR (SUPPRIMER LE MOT QUI N'EST PAS SUR LA LISTE)
# TODO 2: UTILISER STOP_WORDS (OPENCLASSROOMS, paris, : GOOGLE, WIKIPEDIA)
# TODO 3: LIER LE BACKEND ET LE FRONTEND AVEC UNE REQUETTE AJAX (LA REPONSE A ENVOYER AU FRONTEND EN AJAX)
# TODO 4: LES EXPRESSIONS REGULIERES EN PYTHON (A VOIR)
#
