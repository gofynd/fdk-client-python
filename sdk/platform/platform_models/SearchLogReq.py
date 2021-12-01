"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema














class SearchLogReq(BaseSchema):

    
    marketplace_name = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    identifier_value = fields.Str(required=False)
    

