"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class PhoneProperties(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    number = fields.Str(required=False)
    

