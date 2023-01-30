"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CouponDetails(BaseSchema):
    # Cart swagger.json

    
    discount_single_quantity = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    discount_total_quantity = fields.Float(required=False)
    

