"""discount Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .DiscountItems import DiscountItems



class BulkDiscount(BaseSchema):
    #  swagger.json

    
    company_id = fields.Int(required=False)
    
    items = fields.List(fields.Nested(DiscountItems, required=False), required=False)
    
