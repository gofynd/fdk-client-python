"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ActionPage(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
