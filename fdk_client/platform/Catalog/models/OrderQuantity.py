"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OrderQuantity(BaseSchema):
    #  swagger.json

    
    minimum = fields.Int(required=False)
    
    is_set = fields.Boolean(required=False)
    
    maximum = fields.Int(required=False)
    
