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









from .CompanyBrandDocumentsResponseSerializer import CompanyBrandDocumentsResponseSerializer


class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    documents = fields.List(fields.Nested(CompanyBrandDocumentsResponseSerializer, required=False), required=False)
    

