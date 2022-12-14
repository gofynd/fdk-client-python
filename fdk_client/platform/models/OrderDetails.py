"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OrderDetails(BaseSchema):
    # Order swagger.json

    
    created_at = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    

