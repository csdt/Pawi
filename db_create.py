#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from app import db

db.create_all()

db.session.commit()


