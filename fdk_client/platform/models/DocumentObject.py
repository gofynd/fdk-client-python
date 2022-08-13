"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DocumentObject(BaseSchema):
    # CompanyProfile swagger.json

    
    unverified = fields.Int(required=False)
    
    correction_requested = fields.Int(required=False)
    

