"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














































class BillingInfo(BaseSchema):
    #  swagger.json

    
    first_name = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    primary_mobile_number = fields.Str(required=False)
    
    alternate_email = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    floor_no = fields.Str(required=False)
    
    alternate_mobile_number = fields.Str(required=False)
    
    house_no = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    primary_email = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    customer_code = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    middle_name = fields.Str(required=False)
    
    external_customer_code = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
