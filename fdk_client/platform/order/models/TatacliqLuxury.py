"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class TatacliqLuxury(BaseSchema):
    #  swagger.json

    
    sku = fields.Str(required=False)
    
