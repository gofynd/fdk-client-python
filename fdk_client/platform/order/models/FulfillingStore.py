"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




























class FulfillingStore(BaseSchema):
    #  swagger.json

    
    country = fields.Str(required=False)
    
    fulfillment_channel = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    address = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
