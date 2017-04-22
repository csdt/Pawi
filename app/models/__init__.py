#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from .. import admin, app, db
from flask_admin.contrib.sqla import ModelView

from .user import *


admin.add_view(ModelView(User, db.session))

