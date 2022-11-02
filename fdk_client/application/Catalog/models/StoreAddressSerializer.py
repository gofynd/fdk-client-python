"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






















class StoreAddressSerializer(BaseSchema):
    #  swagger.json

    
    landmark = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    address1 = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    latitude = fields.Float(required=False)
    
    country = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    