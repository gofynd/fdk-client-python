"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ProductSize(BaseSchema):
    #  swagger.json

    
    is_available = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    value = fields.Str(required=False)
    
