"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserSerializer import UserSerializer









from .UserSerializer import UserSerializer

from .UserSerializer import UserSerializer



from .CompanySerializer import CompanySerializer

from .GetBrandResponseSerializer import GetBrandResponseSerializer






class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    warnings = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    

