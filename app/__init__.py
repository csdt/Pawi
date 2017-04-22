#! /usr/bin/env python3
# -*-coding:utf-8 -*-

### Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

### config
app = Flask("Pawi")
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
admin = Admin()
admin.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

### Internal imports
from .controllers import *
from .models import *

