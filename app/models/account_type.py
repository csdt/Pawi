#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
__all__ = ["AccountType"]


class AccountType(db.Model):
    __tablename__ = "account_types"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def __init__(self, name = "", description = "", owner = None):
        self.name = name
        self.description = description
        self.owner = owner

    def __repr__(self):
        return "<AccountType {}>".format(self.name)

    def __str__(self):
        return self.name

