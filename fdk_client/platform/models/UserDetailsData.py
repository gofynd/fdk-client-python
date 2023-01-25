"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class UserDetailsData(BaseSchema):
    # Order swagger.json

    
    address = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    

