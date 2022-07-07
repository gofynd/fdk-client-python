"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CompanyBrandDocumentsSerializer import CompanyBrandDocumentsSerializer


class CompanyBrandPostRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    document_required = fields.Boolean(required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
    company = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(CompanyBrandDocumentsSerializer, required=False), required=False)
    

