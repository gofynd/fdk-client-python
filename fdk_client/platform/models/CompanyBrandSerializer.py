"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserSerializer import UserSerializer





from .UserSerializer import UserSerializer

from .CompanyBrandDocumentsResponseSerializer import CompanyBrandDocumentsResponseSerializer





from .UserSerializer import UserSerializer



from .CompanySerializer import CompanySerializer





from .GetBrandResponseSerializer import GetBrandResponseSerializer




class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    documents = fields.List(fields.Nested(CompanyBrandDocumentsResponseSerializer, required=False), required=False)
    
    reject_reason = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    uid = fields.Int(required=False)
    

