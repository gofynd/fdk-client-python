"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SeoDetail(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
