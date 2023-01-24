#!/usr/bin/python3
"""View for place objects that handles all default RESTFul API actions"""


from api.v1.views import app_views
from flask import request, make_response, jsonify, abort
from models import storage
from models.place import Place


@app_views.route('/places', methods=['GET'], strict_slashes=False)
def get_places():
    """Retrieves the list of all place objects"""
    places = []
    for place in storage.all(Place).values():
        places.append(place.to_dict())
    return jsonify(places)


@app_views.route('/places/<string:place_id>', methods=['GET'],
                 strict_slashes=False)
def get_particular_place(place_id):
    """Retrieves a place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<string:place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Deletes a place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places', methods=['POST'], strict_slashes=False)
def create_place():
    """Creates a place object"""
    json_data = request.get_json()
    if json_data is None:
        abort(jsonify(error="Not a JSON", status=400))
    if 'email' not in json_data:
        abort(jsonify(error="Missing email", status=400))
    if 'password' not in json_data:
        abort(jsonify(error="Missing password", status=400))
    place = Place(**request.get_json())
    place.save()
    return make_response(jsonify(place.to_dict()), 201)


@app_views.route('/places/<string:place_id>', methods=['PUT'],
                 strict_slashes=False)
def put_place(place_id):
    """update a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(place, attr, val)
    place.save()
    return jsonify(place.to_dict())
