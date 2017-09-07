#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
__all__ = ["AccountType"]


class AccountType(db.Model):
    __tablename__ = "account_types"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False, default = "")
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = True)
    accounts = db.relationship("Account", backref = "type")

    def __repr__(self):
        return "<AccountType {}>".format(self.name)

    def __str__(self):
        return self.name

    def create(self, **kwargs):
        account = Account(**kwargs)
        account.type = self
        return account

    def copy(self, user = False):
        accountT = make_transient(self)
        accountT._oid = None
        if user is not False:
            accountT.owner = user
        return accountT
