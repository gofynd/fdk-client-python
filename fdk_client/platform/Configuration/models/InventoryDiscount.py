"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InventoryDiscount(BaseSchema):
    #  swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
