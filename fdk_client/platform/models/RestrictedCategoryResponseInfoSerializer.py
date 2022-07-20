"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .RestrictedCategoryFiles import RestrictedCategoryFiles







from .StageReasonResponse import StageReasonResponse










class RestrictedCategoryResponseInfoSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    primary = fields.Boolean(required=False)
    
    store_id = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(RestrictedCategoryFiles, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    document_type = fields.Str(required=False)
    
    stage_reason = fields.List(fields.Nested(StageReasonResponse, required=False), required=False)
    
    value = fields.Str(required=False)
    
    category_type = fields.Str(required=False)
    
    expiry_date = fields.Str(required=False)
    
    issue_date = fields.Str(required=False)
    

