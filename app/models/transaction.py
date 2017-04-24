#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db, Account
import datetime
__all__ = ["Transaction"]

transaction_tag_links = db.Table('transaction_tag_links',
    db.Column('transaction_id', db.Integer, db.ForeignKey('transactions.id')),
    db.Column('transaction_tag_id', db.Integer, db.ForeignKey('transaction_tags.id'))
)
class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float, nullable = False)
    expected_date = db.Column(db.DateTime, nullable = False)
    debit_date = db.Column(db.DateTime, nullable = True)
    credit_date = db.Column(db.DateTime, nullable = True)
    description = db.Column(db.Text, nullable = False, default = "")
    type_id = db.Column(db.Integer, db.ForeignKey('transaction_types.id'))

    creditor_account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable = True)
    debtor_account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable = True)

    creditor_account = db.relationship("Account", foreign_keys=creditor_account_id, primaryjoin=creditor_account_id == Account.id, backref="credits")
    debtor_account = db.relationship("Account", foreign_keys=debtor_account_id, primaryjoin=debtor_account_id == Account.id, backref="debits")

    tags = db.relationship("TransactionTag", secondary = transaction_tag_links, backref = "transactions")



    

    def __init__(self, name = None, **kwargs):
        self.name = name
        self.amount = kwargs.get("amount", None)
        self.open_date = kwargs.get("open_date", None)
        self.description = kwargs.get("description", None)
        self.owner = kwargs.get("owner", None)
        self.type = kwargs.get("type", None)

    def __repr__(self):
        return "<Transaction {}: {} -> {}>".format(self.amount, self.debitor_account, self.creditor_account)

    def __str__(self):
        return "{}({}->{})".format(self.amount, self.debitor_account, self.creditor_account)

