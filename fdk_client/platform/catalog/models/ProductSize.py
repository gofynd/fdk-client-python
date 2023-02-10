"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ProductSize(BaseSchema):
    #  swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    
