"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








































class PlatformDeliveryAddress(BaseSchema):
    #  swagger.json

    
    pincode = fields.Str(required=False)
    
    longitude = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    latitude = fields.Int(required=False)
    
    area = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
