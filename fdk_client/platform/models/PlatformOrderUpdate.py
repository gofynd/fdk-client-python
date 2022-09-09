"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class PlatformOrderUpdate(BaseSchema):
    # OrderManage swagger.json

    
    order_id = fields.Str(required=False)
    

