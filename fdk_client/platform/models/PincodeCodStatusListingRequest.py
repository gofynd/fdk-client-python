"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PincodeCodStatusListingRequest(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    pincode = fields.Int(required=False)
    
    current_page_number = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    

