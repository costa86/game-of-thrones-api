import requests

lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""


# base_url = "http://localhost:5000/v1"
base_url = "http://134.209.232.100:5000/v1"

def get_request(url):
    headers = {
        "Content-Type":"application/json"
    }
    r = requests.get(url=url,headers=headers)
    return r.json()


def post_request(url,json_data):
    headers = {
        "Content-Type":"application/json"
    }
    r = requests.post(url=url,headers=headers,json=json_data)
    return r.json()



# episode_info = get_request(f"{base_url}/episodes?id=6147368b8e5efc0b9b208b34")
# post_comment = post_request(f"{base_url}/comments/episodes",{"comment":"really Bad","id":"6147368b8e5efc0b9b208b34"})
# comments_by_episode = get_request(f"{base_url}/comments/episodes?id=6147368b8e5efc0b9b208b34")
delete_comment = get_request(f"{base_url}/comments/delete?id=61474fd32fd0ed2f706a4fd5")
# edit_comment = post_request(f"{base_url}/comments",{"newText":lorem_ipsum,"id":"61474fb698796a6e5a5ce624"})
# episodes_rating = get_request(f"{base_url}/episodes/ratings/above?rating=9.5&season=3")
# episodes_rating_season = get_request(f"{base_url}/episodes/ratings/above?rating=9&season=7")

print(delete_comment)