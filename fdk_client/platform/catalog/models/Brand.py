"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Logo import Logo





class Brand(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Logo, required=False)
    
    uid = fields.Int(required=False)
    
