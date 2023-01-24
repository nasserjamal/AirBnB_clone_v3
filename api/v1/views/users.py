#!/usr/bin/python3
"""View for User objects that handles all default RESTFul API actions"""


from api.v1.views import app_views
from flask import request, make_response, jsonify, abort
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = []
    for user in storage.all(User).values():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<string:user_id>', methods=['GET'],
                 strict_slashes=False)
def get_particular_user(user_id):
    """Retrieves a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<string:user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a user object"""
    try:
        if request.headers.get("Content-Type", "") == "application/json":
            json_data = request.get_json()
        else:
            raise
    except Exception:
        return make_response("Not a JSON", 400)
    if 'email' not in json_data:
        abort(jsonify(error="Missing email", status=400))
    if 'password' not in json_data:
        abort(jsonify(error="Missing password", status=400))
    user = User(**request.get_json())
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route('/users/<string:user_id>', methods=['PUT'],
                 strict_slashes=False)
def put_user(user_id):
    """update a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    try:
        if request.headers.get("Content-Type", "") == "application/json":
            request_data = request.get_json()
        else:
            raise
    except Exception:
        return make_response("Not a JSON", 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, attr, val)
    user.save()
    return jsonify(user.to_dict())
