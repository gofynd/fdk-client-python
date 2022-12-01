"""share Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class SocialMediaTags(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
