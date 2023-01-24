#!/usr/bin/python3
"""A view for the reviews class"""


from api.v1.views import app_views, jsonify, abort
from flask import request, make_response
from models import storage
from models.place import Place
from models.review import Review


@app_views.route("/places/<place_id>/reviews", strict_slashes=False)
def get_reviews(place_id):
    """Fetches all reviews in the places id"""
    all_reviews = storage.all(Review)
    reviews_in_place = \
        [rv.to_dict() for rv in all_reviews.values()
         if rv.to_dict().get("place_id") == place_id]
    if len(reviews_in_place) == 0:
        abort(404)
    return jsonify(reviews_in_place)


@app_views.route("/reviews/<review_id>", methods=["GET"], strict_slashes=False)
def get_review(review_id=None):
    """Fetches the review with the provided id"""
    rvw = storage.get(Review, review_id)
    if rvw is None:
        abort(404)
    return jsonify(rvw.to_dict())


@app_views.route("/reviews/<review_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_review(review_id=None):
    """Deletes the review with the provided id"""
    rvw = storage.get(Review, review_id)
    if rvw is None:
        abort(404)
    rvw.delete()
    storage.save()
    return jsonify({})


@app_views.route("/places/<place_id>/reviews", methods=["POST"],
                 strict_slashes=False)
def post_review(place_id):
    """Creates a new review"""
    place = storage.get(place, place_id)
    if place is None:
        abort(404)
    try:
        request_data = request.get_json()
    except Exception:
        return make_response("Not a JSON", 400)
    if request_data.get("name") is None:
        return make_response("Missing name", 400)
    new_review = Review(**request_data)
    new_review.place_id = place_id
    new_review.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route("/reviews/<review_id>", methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id):
    """Updates the review with the review id using the values passed"""
    rvw = storage.get(Review, review_id)
    if rvw is None:
        abort(404)
    try:
        if request.headers.get("Content-Type", "") == "application/json":
            request_data = request.get_json()
        else:
            raise
    except Exception:
        return make_response("Not a JSON", 400)
    for key, val in request_data.items():
        if key != "id" or key != "created_at" or key != "updated_at" or\
         key != "user_id" or key != "city_id":
            setattr(rvw, key, val)
    rvw.save()
    return jsonify(rvw.to_dict()), 200
