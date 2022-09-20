"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetBrandResponseSerializer import GetBrandResponseSerializer

from .CompanySerializer import CompanySerializer

from .CompanyBrandDocumentsResponseSerializer import CompanyBrandDocumentsResponseSerializer












class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    documents = fields.List(fields.Nested(CompanyBrandDocumentsResponseSerializer, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    reject_reason = fields.Str(required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    uid = fields.Int(required=False)
    

