"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .UserSerializer1 import UserSerializer1

from .UserSerializer1 import UserSerializer1

from .GetBrandResponseSerializer import GetBrandResponseSerializer

from .GetCompanySerializer import GetCompanySerializer





from .UserSerializer1 import UserSerializer1






class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    reject_reason = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    verified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    

