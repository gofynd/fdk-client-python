"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















from .AffiliateAppConfigMeta import AffiliateAppConfigMeta





class AffiliateAppConfig(BaseSchema):
    #  swagger.json

    
    owner = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    meta = fields.List(fields.Nested(AffiliateAppConfigMeta, required=False), required=False)
    
    description = fields.Str(required=False)
    
