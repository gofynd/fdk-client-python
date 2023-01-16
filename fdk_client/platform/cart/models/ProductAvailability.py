"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ProductAvailability(BaseSchema):
    #  swagger.json

    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    deliverable = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
