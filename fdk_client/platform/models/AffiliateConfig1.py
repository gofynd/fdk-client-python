"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
































class AffiliateConfig1(BaseSchema):
    # Order swagger.json

    
    meta = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    owner = fields.Str(required=False)
    
    dp_assignment = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    app_company_id = fields.Int(required=False)
    
    token = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    force_reassignment = fields.Boolean(required=False)
    
    stores = fields.List(fields.Int(required=False), required=False)
    
    secret = fields.Str(required=False)
    
    ac_id = fields.Str(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    post_order_reassignment = fields.Boolean(required=False)
    

