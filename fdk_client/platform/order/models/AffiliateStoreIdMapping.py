"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class AffiliateStoreIdMapping(BaseSchema):
    #  swagger.json

    
    marketplace_store_id = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
