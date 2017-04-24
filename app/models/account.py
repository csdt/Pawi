#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
import datetime
__all__ = ["Account"]


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    open_date = db.Column(db.DateTime, nullable = False, default = db.func.now())
    description = db.Column(db.Text, nullable = False, default = "")
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    type_id = db.Column(db.Integer, db.ForeignKey('account_types.id'))
    sharings = db.relationship("AccountSharing", backref = "account", cascade = "all, delete-orphan")
    

    def __init__(self, name = None, **kwargs):
        self.name = name
        self.open_date = kwargs.get("open_date", None)
        self.description = kwargs.get("description", None)
        self.owner = kwargs.get("owner", None)
        self.type = kwargs.get("type", None)

    def __repr__(self):
        return "<Account {}.{}>".format(self.owner, self.name)

    def __str__(self):
        return "{}.{}".format(self.owner, self.name)

