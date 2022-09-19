"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetBrandResponseSerializer import GetBrandResponseSerializer





from .CompanyBrandDocumentsResponseSerializer import CompanyBrandDocumentsResponseSerializer





from .CompanySerializer import CompanySerializer




class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(CompanyBrandDocumentsResponseSerializer, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    reject_reason = fields.Str(required=False)
    

