import requests


class Wikipedia:
    def search_for_pages(self, lat, lng):
        params = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 10000,
            "gscoord": f"{lat}|{lng}",
            "format": "json",
        }

        url = "https://fr.wikipedia.org/w/api.php"
        r = requests.get(url, params=params)
        if r.status_code == 200:
            data = r.json()
            return data["query"]["geosearch"]
        return []

    def search_for_page_content(self, id):
        params = {
            "action": "query",
            "prop": "extracts|info",
            "explaintext": "",
            "pageids": id,
            "inprop": "url",
            "format": "json",
            "exchars": 300,
        }

        url = "https://fr.wikipedia.org/w/api.php"
        r = requests.get(url, params=params)
        if r.status_code == 200:
            data = r.json()
            url_page = data['query']['pages'][str(id)]['fullurl']
            intro = data['query']['pages'][str(id)]['extract']
            return intro, url_page
        return []