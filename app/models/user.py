#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
from .account import *
from .account_sharing import *
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
__all__ = ["User"]


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)

    # account
    account_types = db.relationship("AccountType", backref = "owner", cascade = "all, delete-orphan")
    accounts = db.relationship("Account", backref = "owner", cascade = "all, delete-orphan")

    # account sharing
    account_sharing_types = db.relationship("AccountSharingType", backref = "owner", cascade = "all, delete-orphan")
    account_sharings = db.relationship("AccountSharing", backref = "recipient", cascade = "all, delete-orphan")

    accounts_shared = db.relationship("Account", secondary = "account_sharings", viewonly = True)

    # transaction
    transaction_types = db.relationship("TransactionType", backref = "owner", cascade = "all, delete-orphan")
    transaction_tags = db.relationship("TransactionTag", backref = "owner", cascade = "all, delete-orphan")

    def __repr__(self):
        return "<User {}>".format(self.name)

    def __str__(self):
        return self.name

    @hybrid_method
    def can_debit(self, account):
        return account in self.accounts or account in self.accounts_shared
    @can_debit.expression
    def can_debit(self, account):
        return db.or_(self.accounts.contains(account), self.accounts_shared.contains(account))
        #return db.or_(self.accounts.contains(account), self.accounts_shared.any(db.and_(AccountSharing.account == account, ...)))

    @hybrid_method
    def can_credit(self, account):
        return account in self.accounts or account in self.accounts_shared
    @can_debit.expression
    def can_credit(self, account):
        return db.or_(self.accounts.contains(account), self.accounts_shared.contains(account))
        #return db.or_(self.accounts.contains(account), self.accounts_shared.any(db.and_(AccountSharing.account == account, ...)))

