"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class AffiliateAppConfigMeta(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
