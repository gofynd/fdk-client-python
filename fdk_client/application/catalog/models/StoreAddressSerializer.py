"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






















class StoreAddressSerializer(BaseSchema):
    #  swagger.json

    
    city = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    state = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    pincode = fields.Int(required=False)
    
    country = fields.Str(required=False)
    
