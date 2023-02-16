"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class AppOrderConfig(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    force_reassignment = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
