"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CompanySerializer import CompanySerializer







from .GetBrandResponseSerializer import GetBrandResponseSerializer

from .CompanyBrandDocumentsResponseSerializer import CompanyBrandDocumentsResponseSerializer


class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    reject_reason = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    documents = fields.List(fields.Nested(CompanyBrandDocumentsResponseSerializer, required=False), required=False)
    

