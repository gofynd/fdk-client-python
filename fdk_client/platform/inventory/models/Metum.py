"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Metum(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
