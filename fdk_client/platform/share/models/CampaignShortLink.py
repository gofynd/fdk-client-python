"""share Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CampaignShortLink(BaseSchema):
    #  swagger.json

    
    source = fields.Str(required=False)
    
    medium = fields.Str(required=False)
    
