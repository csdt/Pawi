#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
__all__ = ["TransactionType"]


class TransactionType(db.Model):
    __tablename__ = "transaction_types"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False, default = "")
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    transactions = db.relationship("Transaction", backref = "type")

    def __repr__(self):
        return "<TransactionType {}>".format(self.name)

    def __str__(self):
        return self.name

    def create(self, **kwargs):
        transaction = Transaction(**kwargs)
        transaction.type = self
        return transaction

    def copy(self, user = False):
        transactionT = make_transient(self)
        transactionT._oid = None
        if user is not False:
            transactionT.owner = user
        return transactionT
