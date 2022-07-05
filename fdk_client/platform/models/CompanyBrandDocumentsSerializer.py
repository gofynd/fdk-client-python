"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CompanyBrandDocumentsSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

