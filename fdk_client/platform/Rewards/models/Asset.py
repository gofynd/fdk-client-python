"""Rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Asset(BaseSchema):
    #  swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
