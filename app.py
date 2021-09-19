from flask import Flask, render_template, request
from helpers import api_version,db,Episodes,comment_create,comment_delete,comment_get_by_episode,\
    comment_edit,episodes_get_ratings_above,validate_season,validate_rating


app = Flask(__name__)

@app.route("/")
def index():

    episodes = db.episodes.find()

    context = {
        "episodes":episodes,
        "title":"All episodes"
    }
    return render_template("index.html", **context)


@app.route(f"/{api_version}/episodes")
def episodes_get_api():
    id = request.args.get("id")
    try:
        ep = Episodes.get(id)
        res = {
            "Title":ep.title,
            "Season":ep.season,
            "_id":str(ep.id),
            "imdbRating":ep.imdb_rating,
            "Episode":ep.number
            }
        return res
    except:
        return {"error":"episode not found"}


@app.route(f"/{api_version}/episodes/ratings/above")
def episodes_rating_greater_than_api():
    rating = request.args.get("rating")
    season = request.args.get("season") 

    if not validate_rating(request):
        return {"error":"rating is required and it needs to be a number"}

    if not validate_season(request):
        return {"error":"if season is provided, it needs to be a number ranged from 1-8"}

    rating = str(rating)
    episodes = episodes_get_ratings_above(rating)

    if season:
        season = str(season)
        episodes = episodes_get_ratings_above(rating,season)

    return {"episodes":episodes,"quantity":len(episodes)}
    

@app.route(f"/{api_version}/comments/episodes",methods=["POST"])
def comments_create_api():
    if request.method != "POST":
        return {"error":"POST is required"}
        
    id = request.json["id"]
    comment = request.json["comment"]
    try:
        ep = Episodes.get(id)
        comment_create(ep,comment)
        return {"comment":comment}
    except:
        return {"error":"episode not found"}


@app.route(f"/{api_version}/comments",methods=["POST"])
def comments_edit_api():
    if request.method != "POST":
        return {"error":"POST is required"}
        
    id = request.json["id"]
    new_text = request.json["newText"]
    comment_edit(id,new_text)
    return {"comment":new_text}


@app.route(f"/{api_version}/comments/episodes",methods=["GET"])
def comments_get_by_episode_api():
    if request.method != "GET":
        return {"error":"GET is required"}
    try:
        episode_id = request.args.get("id")
        comments = comment_get_by_episode(episode_id) 
        return {"comments":comments,"quantity":len(comments)}
    except:
        return {"error":"episode not found"}


@app.route(f"/{api_version}/comments/delete",methods=["GET"])
def comments_delete_api():
    if request.method != "GET":
        return {"error":"GET is required"}

    id = request.args.get("id")
    comment_delete(id)
    return {"commentDeleted":id}


if __name__ == "main":
    app.run()
