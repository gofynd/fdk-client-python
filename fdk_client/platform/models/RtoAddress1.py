"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .StoreAddress import StoreAddress






















class RtoAddress1(BaseSchema):
    # Order swagger.json

    
    country = fields.Str(required=False)
    
    rtoa_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    contact_person = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    store_address_json = fields.Nested(StoreAddress, required=False)
    
    longitude = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    location_type = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    pincode = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    

