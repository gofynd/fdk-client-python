"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























class StoreReassign(BaseSchema):
    #  swagger.json

    
    store_id = fields.Int(required=False)
    
    item_id = fields.Str(required=False)
    
    reason_ids = fields.List(fields.Int(required=False), required=False)
    
    bag_id = fields.Int(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    set_id = fields.Str(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    
    mongo_article_id = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
