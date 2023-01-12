"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Affiliate import Affiliate







from .AffiliateStoreIdMapping import AffiliateStoreIdMapping


class OrderConfig(BaseSchema):
    # Order swagger.json

    
    create_user = fields.Boolean(required=False)
    
    affiliate = fields.Nested(Affiliate, required=False)
    
    article_lookup = fields.Str(required=False)
    
    bag_end_state = fields.Str(required=False)
    
    store_lookup = fields.Str(required=False)
    
    affiliate_store_id_mapping = fields.List(fields.Nested(AffiliateStoreIdMapping, required=False), required=False)
    

