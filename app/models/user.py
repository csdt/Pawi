#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
__all__ = ["User"]


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)

    def __init__(self, name = "", email = ""):
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User {}>".format(self.name)

    def __str__(self):
        return self.name
