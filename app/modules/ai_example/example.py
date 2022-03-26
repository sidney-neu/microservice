#!/usr/bin/env python
# coding: utf-8
from flask import jsonify

class example_hello():
    def __init__(self):
        pass
    def print_something(self):
        return jsonify({"msg": "hello world"})
