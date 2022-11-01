"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class SegmentCredentials(BaseSchema):
    #  swagger.json

    
    write_key = fields.Str(required=False)
    
