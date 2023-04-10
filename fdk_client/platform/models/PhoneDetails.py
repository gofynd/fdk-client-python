"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PhoneDetails(BaseSchema):
    # Order swagger.json

    
    country_code = fields.Int(required=False)
    
    mobile_number = fields.Str(required=False)
    

