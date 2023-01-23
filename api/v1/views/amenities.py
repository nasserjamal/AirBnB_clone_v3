#!/usr/bin/python3
"""A view for the amenities class"""


from api.v1.views import app_views, jsonify, abort
from flask import request, make_response
from models import storage
from models.amenity import Amenity


@app_views.route("/amenities", methods=['GET'], strict_slashes=False)
def get_all_amenities():
    """Fetches all amenities"""
    all_amenities = storage.all(Amenity)
    return jsonify([amn.to_dict() for amn in all_amenities.values()])


@app_views.route("/amenities/<amenity_id>", methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """Fetches amenities with the specified id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return amenity.to_dict()


@app_views.route("/amenities/<amenity_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """Delete the specified amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route("/amenities", methods=['POST'], strict_slashes=False)
def create_amenity():
    """Creates a new amenity"""
    try:
        request_data = request.get_json()
    except Exception:
        return make_response("Not a JSON", 400)
    if request_data.get("name") is None:
        return make_response("Missing name", 400)
    new_amenity = Amenity(**request_data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route("/amenities/<amenity_id>", methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """Update an amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    try:
        request_data = request.get_json()
    except Exception:
        return make_response("Not a JSON", 400)
    for key, val in request_data.items():
        if key != "id" or key != "created_at" or key != "updated_at":
            setattr(amenity, key, val)
    amenity.save()
    return jsonify(amenity.to_dict())
