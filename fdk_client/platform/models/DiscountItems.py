"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class DiscountItems(BaseSchema):
    # Discount swagger.json

    
    item_code = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    value = fields.Float(required=False)
    

