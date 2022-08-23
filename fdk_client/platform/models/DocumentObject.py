"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DocumentObject(BaseSchema):
    # CompanyProfile swagger.json

    
    correction_requested = fields.Int(required=False)
    
    unverified = fields.Int(required=False)
    

