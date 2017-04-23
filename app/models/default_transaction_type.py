#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
__all__ = ["DefaultTransactionType"]


class DefaultTransactionType(db.Model):
    __tablename__ = "default_transaction_types"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False, default = "")

    def __init__(self, name = "", description = ""):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<DefaultTransactionType {}>".format(self.name)

    def __str__(self):
        return self.name
