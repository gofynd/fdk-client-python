"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ProductAvailability(BaseSchema):
    #  swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    
    deliverable = fields.Boolean(required=False)
    
