#!/usr/bin/python3
"""A view for the cities class"""


from api.v1.views import app_views, jsonify
from models import storage
from models.city import City


@app_views.route("states/<state_id>/cities")
def get_cities(state_id):
    all_cities = storage.all(City)
    cities_in_state = \
        [ct.to_dict() for ct in all_cities.values()
         if ct.to_dict().get("state_id") == state_id]
    return jsonify(cities_in_state)
