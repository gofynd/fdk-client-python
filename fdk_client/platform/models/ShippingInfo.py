"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















































class ShippingInfo(BaseSchema):
    # Order swagger.json

    
    geo_location = fields.Dict(required=False)
    
    address_type = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    customer_code = fields.Str(required=False)
    
    primary_email = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    alternate_mobile_number = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    primary_mobile_number = fields.Str(required=False)
    
    alternate_email = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    floor_no = fields.Str(required=False)
    
    external_customer_code = fields.Str(required=False)
    
    house_no = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    slot = fields.List(fields.Dict(required=False), required=False)
    
    middle_name = fields.Str(required=False)
    
    shipping_type = fields.Str(required=False)
    
    city = fields.Str(required=False)
    

