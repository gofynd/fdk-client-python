"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class NetQuantity(BaseSchema):
    #  swagger.json

    
    value = fields.Float(required=False)
    
    unit = fields.Raw(required=False)
    
