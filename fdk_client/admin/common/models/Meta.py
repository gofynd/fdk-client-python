"""common Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Meta(BaseSchema):
    #  swagger.json

    
    comment = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
