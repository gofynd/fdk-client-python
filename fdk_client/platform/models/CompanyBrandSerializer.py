"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CompanyBrandDocumentsResponseSerializer import CompanyBrandDocumentsResponseSerializer





from .CompanySerializer import CompanySerializer



from .UserSerializer import UserSerializer

from .GetBrandResponseSerializer import GetBrandResponseSerializer



from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer








class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    documents = fields.List(fields.Nested(CompanyBrandDocumentsResponseSerializer, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    uid = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    reject_reason = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    

