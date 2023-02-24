"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GiveawayAudience(BaseSchema):
    # Rewards swagger.json

    
    audience_id = fields.Str(required=False)
    
    current_count = fields.Float(required=False)
    

