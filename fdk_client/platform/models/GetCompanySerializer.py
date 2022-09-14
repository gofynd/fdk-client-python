"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .BaseUserSerializer import BaseUserSerializer



from .GetAddressSerializer import GetAddressSerializer







from .BaseUserSerializer import BaseUserSerializer





from .BaseUserSerializer import BaseUserSerializer




class GetCompanySerializer(BaseSchema):
    # Catalog swagger.json

    
    verified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Nested(BaseUserSerializer, required=False)
    
    reject_reason = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    
    verified_by = fields.Nested(BaseUserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Nested(BaseUserSerializer, required=False)
    
    business_type = fields.Str(required=False)
    

