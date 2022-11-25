"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class StoreReassign(BaseSchema):
    # OrderManage swagger.json

    
    bag_id = fields.Int(required=False)
    
    mongo_article_id = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    set_id = fields.Str(required=False)
    
    reason_ids = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    

