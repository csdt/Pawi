#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
__all__ = ["DefaultTransactionTag"]


class DefaultTransactionTag(db.Model):
    __tablename__ = "default_transaction_tags"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False, default = "")

    def __repr__(self):
        return "<DefaultTransactionTag {}>".format(self.name)

    def __str__(self):
        return self.name

