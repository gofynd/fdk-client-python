"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class NetQuantity1(BaseSchema):
    #  swagger.json

    
    unit = fields.Raw(required=False)
    
    value = fields.Float(required=False)
    
