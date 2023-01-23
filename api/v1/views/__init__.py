#!/usr/bin/python3
"""Wildcard imports and Blueprint instance creation"""


from flask import Blueprint, jsonify, abort
from api.v1.views.index import *
from api.v1.views.cities import *
from api.v1.views.states import *
from api.v1.views.users import *

app_views = Blueprint("app_views", __name__)
