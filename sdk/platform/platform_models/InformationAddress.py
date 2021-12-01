"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .InformationPhone import InformationPhone








class InformationAddress(BaseSchema):

    
    loc = fields.Str(required=False)
    
    address_line = fields.List(fields.Str(required=False), required=False)
    
    phone = fields.Nested(InformationPhone, required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    

