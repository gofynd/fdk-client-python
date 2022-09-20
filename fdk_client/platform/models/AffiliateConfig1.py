"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
































class AffiliateConfig1(BaseSchema):
    # Order swagger.json

    
    owner = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    app_company_id = fields.Int(required=False)
    
    force_reassignment = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    post_order_reassignment = fields.Boolean(required=False)
    
    ac_id = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    stores = fields.List(fields.Int(required=False), required=False)
    
    dp_assignment = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    meta = fields.List(fields.Dict(required=False), required=False)
    
    article_assignment = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    

