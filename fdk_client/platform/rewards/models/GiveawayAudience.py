"""rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class GiveawayAudience(BaseSchema):
    #  swagger.json

    
    audience_id = fields.Str(required=False)
    
    current_count = fields.Float(required=False)
    
