#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.city import City

# print("All objects: {}".format(storage.count()))
# print("State objects: {}".format(storage.count(State)))

stt1 = City()
stt1.name = "San Francisco"
stt1.state_id