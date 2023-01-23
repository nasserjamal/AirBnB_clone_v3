#!/usr/bin/python3
"""I dont know what the **** this is"""


from flask import Blueprint, jsonify, abort

app_views = Blueprint("app_views", __name__)

from api.v1.views.index import *
from api.v1.views.cities import *
from api.v1.views.states import *
