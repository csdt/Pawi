#! /usr/bin/env python3
# -*-coding:utf-8 -*-

import os

CSRF_ENABLED = True
with os.open('key', 'r') as key_file
    SECRET_KEY = key_file.read().strip()

