"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .AffiliateConfig import AffiliateConfig



class Affiliate(BaseSchema):
    #  swagger.json

    
    token = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    config = fields.Nested(AffiliateConfig, required=False)
    
