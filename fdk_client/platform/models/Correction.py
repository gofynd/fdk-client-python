"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Correction(BaseSchema):
    # CompanyProfile swagger.json

    
    reason_code = fields.Str(required=False)
    
    desc = fields.Str(required=False)
    

