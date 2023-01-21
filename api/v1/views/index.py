#!/usr/bin/python3
"""Ata hii sijui ni nini"""

from api.v1.views import app_views, jsonify


@app_views.route("/status")
def index():
    return jsonify({"status": "OK"})
