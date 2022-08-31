"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CompanyBrandDocumentsResponseSerializer import CompanyBrandDocumentsResponseSerializer

from .CompanySerializer import CompanySerializer





from .GetBrandResponseSerializer import GetBrandResponseSerializer


class CompanyBrandSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    uid = fields.Int(required=False)
    
    reject_reason = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(CompanyBrandDocumentsResponseSerializer, required=False), required=False)
    
    company = fields.Nested(CompanySerializer, required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    

