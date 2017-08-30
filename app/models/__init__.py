#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from .. import admin, app, db
from flask_admin.contrib.sqla import ModelView

# currency
from .currency import *

# user
from .user import *

# account
from .account_type import *
from .account import *

# account sharing
from .account_sharing_type import *
from .account_sharing import *

# transaction
from .transaction_type import *
from .transaction_tag import *
from .transaction import *

# currency
admin.add_view(ModelView(Currency, db.session))

# user
admin.add_view(ModelView(User, db.session))

# account
admin.add_view(ModelView(AccountType, db.session))
admin.add_view(ModelView(Account, db.session))

# account sharing
admin.add_view(ModelView(AccountSharingType, db.session))
admin.add_view(ModelView(AccountSharing, db.session))

# transaction
admin.add_view(ModelView(TransactionType, db.session))
admin.add_view(ModelView(TransactionTag, db.session))
admin.add_view(ModelView(Transaction, db.session))

