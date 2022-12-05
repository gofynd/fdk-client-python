"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




































class PickupStoreDetail(BaseSchema):
    #  swagger.json

    
    city = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    address_type = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    area_code = fields.Str(required=False)
    
