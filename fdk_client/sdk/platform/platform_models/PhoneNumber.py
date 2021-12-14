"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class PhoneNumber(BaseSchema):
    # Lead swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    phone = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    

