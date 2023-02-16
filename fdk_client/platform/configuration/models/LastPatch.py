"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class LastPatch(BaseSchema):
    #  swagger.json

    
    op = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
