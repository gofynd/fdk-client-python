"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ProductAvailability(BaseSchema):
    #  swagger.json

    
    other_store_quantity = fields.Int(required=False)
    
    deliverable = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
