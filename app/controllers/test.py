#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app

print("pouet")
 
@app.route('/')
def index():
    return "Hello World!"

