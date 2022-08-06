"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Deactivation(BaseSchema):
    # CompanyProfile swagger.json

    
    reason = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    

