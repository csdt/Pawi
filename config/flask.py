#! /usr/bin/env python3
# -*-coding:utf-8 -*-

import os.path

CSRF_ENABLED = True
with open(os.path.dirname(__file__) + '/key', 'r') as key_file:
    SECRET_KEY = key_file.read().strip()

