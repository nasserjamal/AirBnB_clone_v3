#!/usr/bin/python3
"""The entry point of our restful api"""


from os import getenv
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.errorhandler(404)
def not_found(error):
    """Error handler taking care of 404 error"""
    return make_response(jsonify({"error": "Not found"}), 404)

@app.teardown_appcontext
def on_app_close(ja3):
    """Called when the app is closed. Closes the storage"""
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
