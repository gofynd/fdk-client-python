"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class NetQuantity(BaseSchema):
    #  swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
