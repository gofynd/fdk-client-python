"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InventoryBrand(BaseSchema):
    #  swagger.json

    
    criteria = fields.Str(required=False)
    
    brands = fields.List(fields.Raw(required=False), required=False)
    
