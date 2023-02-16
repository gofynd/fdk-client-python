"""share Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CampaignShortLink(BaseSchema):
    #  swagger.json

    
    source = fields.Str(required=False)
    
    medium = fields.Str(required=False)
    
