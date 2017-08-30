#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from . import app, db
__all__ = ["Currency"]


class Currency(db.Model):
    __tablename__ = "currencies"

    id = db.Column(db.Integer, primary_key = True)
    iso = db.Column(db.String, nullable = False, unique = True)
    name = db.Column(db.String, nullable = False, unique = True)
    symbol = db.Column(db.String, nullable = False)
    left_symbol = db.Column(db.Boolean, nullable = False, default = True)
    space_between = db.Column(db.Boolean, nullable = False, default = True)
    decimals = db.Column(db.Integer, nullable = False, default = 2)
    decimal_separator = db.Column(db.String, nullable = False, default = ".")
    decimal_short = db.Column(db.String, nullable = True, default = ".--")
    group_by = db.Column(db.Integer, nullable = False, default = 3)
    grouping_separator = db.Column(db.String, nullable = False, default = " ")

    def __repr__(self):
        return "<Currency {} ({})>".format(self.symbol, self.iso)

    def __str__(self):
        return "{} ({})".format(self.symbol, self.iso)

    def format(self, amount):
        acc = []
        if self.left_symbol:
            acc.append(self.symbol)
            if self.space_between:
                acc.append(" ")
        if amount < 0:
            acc.append('-')
            amount = -amount

        amount_str = str(amount)
        l = len(amount_str) - self.decimals
        if self.decimals > 0:
            decimal = "0" * max(0, -l) + amount_str[-self.decimals:]
        n = 1 + (l - 1) // self.group_by
        digits = [0]*n
        for i in range(n):
            digits[n-1-i] = amount_str[max(0, l - (i+1)*self.group_by):max(0, l - i*self.group_by)]
            
        if n <= 0:
            digits = [0]

        separator = False
        for dg in digits:
            if separator:
                acc.append(self.grouping_separator)
            separator = True
            acc.append(str(dg))
        if self.decimals > 0:
            if decimal == "0" * self.decimals and self.decimal_short:
                acc.append(self.decimal_short)
            else:
                acc.append(self.decimal_separator)
                acc.append(str(decimal))
        if not self.left_symbol:
            if self.space_between:
                acc.append(" ")
            acc.append(self.symbol)
        return "".join(acc)


