#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
__all__ = ["TransactionTag"]


class TransactionTag(db.Model):
    __tablename__ = "transaction_tags"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False, default = "")
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    #transactions = db.relationship("Transaction", backref = "tag")

    def __repr__(self):
        return "<TransactionTag {}>".format(self.name)

    def __str__(self):
        return self.name


    def copy(self, user = False):
        tag = make_transient(self)
        tag._oid = None
        if user is not False:
            tag.owner = user
        return tag
