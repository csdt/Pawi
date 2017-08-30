#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
import datetime
__all__ = ["AccountSharing"]


class AccountSharing(db.Model):
    __tablename__ = "account_sharings"

    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.DateTime, nullable = False, default = db.func.now())
    end_date = db.Column(db.DateTime)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable = False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    type_id = db.Column(db.Integer, db.ForeignKey('account_sharing_types.id'))

    def __repr__(self):
        return "<AccountSharing {}.{} with {} ({})>".format(self.account.owner, self.account.name, self.recipient, self.type)

    def __str__(self):
        return repr(self)

