"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PageContent(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    
