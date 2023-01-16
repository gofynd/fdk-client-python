"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Media1(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
