#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
__all__ = ["User"]


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    account_types = db.relationship("AccountType", backref = "owner", cascade = "all, delete-orphan")
    accounts = db.relationship("Account", backref = "owner", cascade = "all, delete-orphan")
    account_sharing_types = db.relationship("AccountSharingType", backref = "owner", cascade = "all, delete-orphan")
    account_sharings = db.relationship("AccountSharing", backref = "recipient", cascade = "all, delete-orphan")

    def __init__(self, name = "", email = ""):
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User {}>".format(self.name)

    def __str__(self):
        return self.name
