import requests
import json

URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        ret = response.content
        return ret

    def load_json(self):
        response = requests.get(self.url)
        ret = json.loads(response.content)
        return ret
    
requester = GetRequester(URL)
print(requester.get_response_body())
