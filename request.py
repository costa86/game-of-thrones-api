from typing import Union
import requests
from pprint import pprint

from requests.models import Response


HEADERS = {"Content-Type": "application/json"}
BASE_URL = "http://161.35.68.36:5000/v1"
LAST_EPISODE_ID = "61adffa2323daf7665ef5cbf"


def get_request(url: str) -> Response:
    r = requests.get(url=url, headers=HEADERS)
    return r.json()


def post_request(url: str, json_data: dict) -> Response:
    r = requests.post(url=url, headers=HEADERS, json=json_data)
    return r.json()


#-----API FUNCTIONS-------------------

def get_comments_by_episode(episode_id: str):
    comments_by_episode = get_request(
        f"{BASE_URL}/comments/episodes?id={episode_id}")
    pprint(comments_by_episode)


def edit_comment(comment: str, comment_id: str):
    edit_comment = post_request(
        f"{BASE_URL}/comments", {"newText": comment, "id": comment_id})
    pprint(edit_comment)


def post_comment(comment: str, episode_id: str):
    post_comment = post_request(
        f"{BASE_URL}/comments/episodes", {"comment": comment, "id": episode_id})
    pprint(post_comment)


def get_episode_info(episode_id: str):
    episode_info = get_request(f"{BASE_URL}/episodes?id={episode_id}")
    pprint(episode_info)


def delete_comment(comment_id: str):
    delete_comment = get_request(f"{BASE_URL}/comments/delete?id={comment_id}")
    pprint(delete_comment)


def get_episodes_by_rating_above(rating: float, season: Union[int, None] = None):
    if not season:
        episodes_rating = get_request(
            f"{BASE_URL}/episodes/ratings/above?rating={rating}")
        pprint(episodes_rating)
        return
    episodes_rating = get_request(
        f"{BASE_URL}/episodes/ratings/above?rating={rating}&season={season}")
    pprint(episodes_rating)
    return


get_episodes_by_rating_above(95.8)
