#! /usr/bin/env python3
# -*-coding:utf-8 -*-

from .. import admin, app, db
from flask_admin.contrib.sqla import ModelView

from .user import *
from .default_account_type import *
from .account_type import *
from .account import *
from .default_account_sharing_type import *
from .account_sharing_type import *
from .account_sharing import *

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(DefaultAccountType, db.session))
admin.add_view(ModelView(AccountType, db.session))
admin.add_view(ModelView(Account, db.session))
admin.add_view(ModelView(DefaultAccountSharingType, db.session))
admin.add_view(ModelView(AccountSharingType, db.session))
admin.add_view(ModelView(AccountSharing, db.session))

