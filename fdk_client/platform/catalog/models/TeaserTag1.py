"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class TeaserTag1(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
