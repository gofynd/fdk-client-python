"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Bags1(BaseSchema):
    # Order swagger.json

    
    affiliate_bag_id = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    is_locked = fields.Boolean(required=False)
    

