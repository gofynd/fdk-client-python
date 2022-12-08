"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ProductSize(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
