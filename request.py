import requests
from pprint import pprint

LOREN_IPSUM = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""  
HEADERS = {"Content-Type":"application/json"}
BASE_URL = "http://localhost:5000/v1"

def get_request(url):
    r = requests.get(url=url,headers=HEADERS)
    return r.json()


def post_request(url,json_data):
    r = requests.post(url=url,headers=HEADERS,json=json_data)
    return r.json()

ep_sample = "61a3d27009cac5993a0a5ac3"

# edit_comment = post_request(f"{BASE_URL}/comments",{"newText":"ok, I guess...","id":"61a3d3c2041bbe209837455b"})
# episode_info = get_request(f"{BASE_URL}/episodes?id={ep_sample}")
# post_comment = post_request(f"{BASE_URL}/comments/episodes",{"comment":"really Bad","id":ep_sample})
comments_by_episode = get_request(f"{BASE_URL}/comments/episodes?id={ep_sample}")
# delete_comment = get_request(f"{BASE_URL}/comments/delete?id=61474fd32fd0ed2f706a4fd5")
# episodes_rating = get_request(f"{BASE_URL}/episodes/ratings/above?rating=9.5&season=3")
# episodes_rating_season = get_request(f"{BASE_URL}/episodes/ratings/above?rating=5&season=8")

pprint(comments_by_episode)