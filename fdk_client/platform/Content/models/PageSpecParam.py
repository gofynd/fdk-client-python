"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PageSpecParam(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
