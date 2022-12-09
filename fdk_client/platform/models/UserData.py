"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderUser import OrderUser

from .OrderUser import OrderUser


class UserData(BaseSchema):
    # OrderManage swagger.json

    
    shipping_user = fields.Nested(OrderUser, required=False)
    
    billing_user = fields.Nested(OrderUser, required=False)
    

