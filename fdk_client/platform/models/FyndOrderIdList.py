"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class FyndOrderIdList(BaseSchema):
    # OrderManage swagger.json

    
    fynd_order_id = fields.List(fields.Str(required=False), required=False)
    

