"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























class OrderUser(BaseSchema):
    #  swagger.json

    
    first_name = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    mobile = fields.Int(required=False)
    
    email = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    phone = fields.Int(required=False)
    
    pincode = fields.Str(required=False)
    
