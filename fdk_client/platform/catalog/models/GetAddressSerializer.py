"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























class GetAddressSerializer(BaseSchema):
    #  swagger.json

    
    address2 = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    address1 = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    pincode = fields.Int(required=False)
    
