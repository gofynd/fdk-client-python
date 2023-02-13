"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








































class StoreAddress(BaseSchema):
    # Orders swagger.json

    
    updated_at = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    address1 = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    landmark = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    city = fields.Str(required=False)
    

