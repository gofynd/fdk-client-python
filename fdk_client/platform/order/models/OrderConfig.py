"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AffiliateStoreIdMapping import AffiliateStoreIdMapping





from .Affiliate import Affiliate









class OrderConfig(BaseSchema):
    #  swagger.json

    
    affiliate_store_id_mapping = fields.List(fields.Nested(AffiliateStoreIdMapping, required=False), required=False)
    
    create_user = fields.Boolean(required=False)
    
    affiliate = fields.Nested(Affiliate, required=False)
    
    article_lookup = fields.Str(required=False)
    
    store_lookup = fields.Str(required=False)
    
    bag_end_state = fields.Str(required=False)
    
