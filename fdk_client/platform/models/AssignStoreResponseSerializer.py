"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





















from ._ArticleAssignment import _ArticleAssignment










class AssignStoreResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    _id = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    
    index = fields.Int(required=False)
    
    store_pincode = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    preice_effective = fields.Float(required=False)
    
    s_city = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    article_assignment = fields.Nested(_ArticleAssignment, required=False)
    
    price_marked = fields.Float(required=False)
    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    

