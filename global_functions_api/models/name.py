# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.


from odoo.models import *
from datetime import datetime
import requests
from odoo import _, api, exceptions, fields, models, modules
from odoo.addons.base.models.res_users import is_selection_groups
from odoo.addons.mail.models.res_users import *


class BaseModelExtend(AbstractModel):


    _inherit = 'base'

    @api.model
    def encode(self,string,SHA=256):
        import hashlib
        if SHA == 512:result = hashlib.sha512(string.encode())
        elif SHA == 384:result = hashlib.sha384(string.encode())
        elif SHA == 256:result = hashlib.sha256(string.encode())
        elif SHA == 224:result = hashlib.sha224(string.encode())
        else:result = hashlib.sha1(string.encode())
        return (result.hexdigest())


    @api.model
    def regex(self,pattern,string,method='f',replace=''):
        import re
        if method == 'r' or method =='replace' or method =='sub':
            return re.sub(pattern,replace,string)
        elif method =='s' or method =='split':
            return re.split(pattern,string)
        else:
            return re.findall(pattern,string)

    @api.model
    def evaluate(self,computation):
        try:return eval(computation)
        except Exception as e:return (e.args[0])
