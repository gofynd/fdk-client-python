"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InventoryBrandRule(BaseSchema):
    #  swagger.json

    
    criteria = fields.Str(required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
