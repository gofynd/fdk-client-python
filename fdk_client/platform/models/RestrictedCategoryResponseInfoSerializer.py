"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RestrictedCategoryFiles import RestrictedCategoryFiles



















from .StageReason import StageReason




class RestrictedCategoryResponseInfoSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    documents = fields.List(fields.Nested(RestrictedCategoryFiles, required=False), required=False)
    
    primary = fields.Boolean(required=False)
    
    category_type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    expiry_date = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    document_type = fields.Str(required=False)
    
    issue_date = fields.Str(required=False)
    
    stage_reason = fields.List(fields.Nested(StageReason, required=False), required=False)
    
    stage = fields.Str(required=False)
    

