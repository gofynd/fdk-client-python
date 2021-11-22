"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .Schedule import Schedule





from .RewardsAudience import RewardsAudience

from .Asset import Asset







from .RewardsRule import RewardsRule






class Giveaway(Schema):

    
    _id = fields.Str(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    audience = fields.Nested(RewardsAudience, required=False)
    
    banner_image = fields.Nested(Asset, required=False)
    
    created_at = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    rule = fields.Nested(RewardsRule, required=False)
    
    title = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    

