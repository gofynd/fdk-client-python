"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Media2(BaseSchema):
    #  swagger.json

    
    landscape = fields.Str(required=False)
    
    portrait = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
