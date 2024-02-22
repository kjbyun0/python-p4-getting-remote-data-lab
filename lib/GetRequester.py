import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())

# URLs to test
# url = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
# url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"
