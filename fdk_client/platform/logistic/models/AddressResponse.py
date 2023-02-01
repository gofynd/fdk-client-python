"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class AddressResponse(BaseSchema):
    #  swagger.json

    
    longitude = fields.Float(required=False)
    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    pincode = fields.Int(required=False)
    
    landmark = fields.Str(required=False)
    
