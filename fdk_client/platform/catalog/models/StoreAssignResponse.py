"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























from .ArticleAssignment1 import ArticleAssignment1













class StoreAssignResponse(BaseSchema):
    #  swagger.json

    
    index = fields.Int(required=False)
    
    group_id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    s_city = fields.Str(required=False)
    
    store_pincode = fields.Int(required=False)
    
    status = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    strategy_wise_listing = fields.List(fields.Dict(required=False), required=False)
    
    price_effective = fields.Int(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment1, required=False)
    
    company_id = fields.Int(required=False)
    
    price_marked = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
