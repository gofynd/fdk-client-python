"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class BusinessCountryInfo(BaseSchema):

    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    

