#! /usr/bin/env python3
# -*-coding:utf-8 -*-

### Imports
from flask import Flask

### config
app = Flask("Pawi")

### Internal imports
from .controllers import *
from .models import *
