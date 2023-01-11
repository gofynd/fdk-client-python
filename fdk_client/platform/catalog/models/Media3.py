"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Media3(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
