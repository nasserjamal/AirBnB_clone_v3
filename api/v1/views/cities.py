#!/usr/bin/python3
"""A view for the cities class"""


from api.v1.views import app_views, jsonify, abort
from flask import request, make_response
from models import storage
from models.city import City
from models.state import State


# @app_views.route("states/<state_id>/cities")
# def get_cities(state_id):
#     """Fetches all cities in the states id"""
#     all_cities = storage.all(City)
#     cities_in_state = \
#         [ct.to_dict() for ct in all_cities.values()
#          if ct.to_dict().get("state_id") == state_id]
#     if len(cities_in_state) == 0:
#         abort(404)
#     return jsonify(cities_in_state)


# @app_views.route("cities/<city_id>", methods=["GET"])
# def get_city(city_id=None):
#     """Fetches the city with the provided id"""
#     cty = storage.get(City, city_id)
#     if cty is None:
#         abort(404)
#     return jsonify(cty.to_dict())


# @app_views.route("cities/<city_id>", methods=["DELETE"])
# def delete_city(city_id=None):
#     """Deletes the city with the city id provided"""
#     cty = storage.get(City, city_id)
#     if cty is None:
#         abort(404)
#     storage.delete(cty)
#     return jsonify({})


# @app_views.route("states/<state_id>/cities", methods=["POST"])
# def post_city(state_id):
#     """Creates a new city"""
#     state = storage.get(State, state_id)
#     if state is None:
#         abort(404)
#     try:
#         request_data = request.get_json()
#     except Exception:
#         return make_response("Not a JSON", 400)
#     if request_data.get("name") is None:
#         return make_response("Missing name", 400)
#     new_city = City()
#     for key, val in request_data.items():
#         setattr(new_city, key, val)
#     new_city.state_id = state_id
#     new_city.save()
#     storage.save()
#     return jsonify(new_city.to_dict()), 201


# @app_views.route("cities/<city_id>", methods=['PUT'])
# def update_city(city_id):
#     """Updates the city with the city id using the values passed"""
#     cty = storage.get(City, city_id)
#     if cty is None:
#         abort(404)
#     try:
#         request_data = request.get_json()
#     except Exception:
#         return make_response("Not a JSON", 400)
#     for key, val in request_data.items():
#         setattr(cty, key, val)
#     cty.save()
#     return jsonify(cty.to_dict()), 200
