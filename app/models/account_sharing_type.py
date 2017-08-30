#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
from sqlalchemy.orm.session import make_transient

__all__ = ["AccountSharingType"]


class AccountSharingType(db.Model):
    __tablename__ = "account_sharing_types"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False, default = "")
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    accounts = db.relationship("AccountSharing", backref = "type")

    def __repr__(self):
        return "<AccountSharingType {}.{}>".format(self.owner, self.name)

    def __str__(self):
        return self.name

    
    def create(self, **kwargs):
        sharing = AccountSharing(**kwargs)
        sharing.type = self
        return sharing

    def copy(self, user = False):
        sharingT = make_transient(self)
        sharingT._oid = None
        if user is not False:
            sharingT.owner = user
        return sharingT
