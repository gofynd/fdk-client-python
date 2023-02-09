"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class TeaserTag1(BaseSchema):
    #  swagger.json

    
    tag = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
