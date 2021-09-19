from pymongo import MongoClient
import os
from bson import ObjectId
import random
import string
import datetime


api_version = "v1"
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
client = MongoClient(f"mongodb://{db_user}:{db_password}@mongo")
db = client.gotdb


def validate_rating(request):
    rating = request.args.get("rating")
    if not rating:
        return False
    try:
        rating = float(rating)
    except:
        return False
    return True


def validate_season(request):
    season = request.args.get("season")
    rating = request.args.get("rating")

    if rating and not season:
        return True
    if season:
        try:
            season = int(season)
            if season not in range(1, 9):
                return False
        except:
            return False
    return True


def get_value_or_default(record, key, default=""):
    try:
        return record[key]
    except:
        return default


def comment_create(episode, comment_text):
    comment = create_comment(episode, comment_text)
    db.comments.insert_one(comment)


def comment_edit(id, new_text):
    db.comments.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {"comment": new_text}
        }
    )


def comment_delete(id):
    db.comments.delete_one({"_id": ObjectId(id)})


def comment_get_by_episode(episode_id: str):
    comments = db.comments.find({"episodeID": ObjectId(episode_id)})
    comments = [
        {
            "comment": i["comment"],
            "creationDate":i["creationDate"],
            "_id":str(i["_id"]),
            "episodeID":str(i["episodeID"])
        } for i in comments]

    return comments


def episodes_get_ratings_above(rating: str, season=None):
    query = {
        "imdbRating": {"$gt": rating}
    }
    if season:
        query.update({"Season": season})

    episodes = db.episodes.find(query)
    episodes = [
        {
            "_id": str(i["_id"]),
            "Title":i["Title"],
            "Released":i["Released"],
            "Episode":i["Episode"],
            "imdbRating":i["imdbRating"],
            "Season":i["Season"],
            "imdbID":i["imdbID"]
        } for i in episodes]

    return episodes


class Episodes:
    def __init__(self, title="na"):
        self.__title = title
        self.__season = "na"
        self.__imdb_rating = "na"
        self.__number = "na"

    def __str__(self):
        return self.__title

    @property
    def title(self):
        return self.__title

    @property
    def season(self):
        return self.__season

    @property
    def id(self):
        return self.__id

    @property
    def imdb_rating(self):
        return self.__imdb_rating

    @property
    def number(self):
        return self.__number

    @title.setter
    def title(self, value):
        self.__title = value

    @season.setter
    def season(self, value):
        self.__season = value

    @id.setter
    def id(self, value):
        self.__id = value

    @imdb_rating.setter
    def imdb_rating(self, value):
        self.__imdb_rating = value

    @number.setter
    def number(self, value):
        self.__number = value

    def save(self):
        "Adds episode to database"
        self.__id = ObjectId()
        db.episodes.insert_one(
            {
                "_id": self.__id,
                "Title": self.__title,
                "Season": self.__season
            }
        )

    def get(id):
        "Gets and episode by '_id'"
        record = db.episodes.find_one(
            {
                "_id": ObjectId(id)
            }
        )
        ep = Episodes(record["Title"])
        ep.id = ObjectId(record["_id"])
        ep.season = get_value_or_default(record, "Season", "")
        ep.imdb_rating = get_value_or_default(record, "imdbRating", "")
        ep.number = get_value_or_default(record, "Episode", "")

        return ep

    def update(self, key, value):
        "Updates any attribute of the episode"
        db.episodes.update_one(
            {"_id": self.__id},
            {"$set": {key: value}
             }
        )

    def delete(self):
        "Deletes the episode from database"
        db.episodes.delete_one(
            {
                "_id": self.__id
            }
        )


def get_ISO8601_UTC():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H:%M")


def create_comment(episode, comment="very good"):
    return {
        "comment": comment,
        "creationDate": get_ISO8601_UTC(),
        "episodeID": episode.id
    }
