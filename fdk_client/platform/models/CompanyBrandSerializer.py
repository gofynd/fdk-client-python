"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .CompanyBrandDocumentsResponseSerializer import CompanyBrandDocumentsResponseSerializer

from .GetBrandResponseSerializer import GetBrandResponseSerializer

from .CompanySerializer import CompanySerializer


class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(CompanyBrandDocumentsResponseSerializer, required=False), required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    

