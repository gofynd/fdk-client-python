"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OrderQuantity(BaseSchema):
    #  swagger.json

    
    is_set = fields.Boolean(required=False)
    
    minimum = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
