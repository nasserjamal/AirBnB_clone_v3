#!/usr/bin/python3
"""Ata hii sijui ni nini"""

from api.v1.views import app_views, jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


stats_data =\
    {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }


@app_views.route("/status")
def index():
    """Returns the status of our api"""
    return jsonify({"status": "OK"})


# @app_views.route("/stats", methods=["GET"])
# def stats():
#     """Returns the number of each of the classes in the database"""
#     return jsonify(stats_data)
