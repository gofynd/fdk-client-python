"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























from ._ArticleAssignment import _ArticleAssignment









class AssignStoreResponseSerializer(BaseSchema):
    #  swagger.json

    
    s_city = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    price_marked = fields.Float(required=False)
    
    uid = fields.Str(required=False)
    
    preice_effective = fields.Float(required=False)
    
    _id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    store_pincode = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    status = fields.Boolean(required=False)
    
    article_assignment = fields.Nested(_ArticleAssignment, required=False)
    
    item_id = fields.Int(required=False)
    
    index = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
