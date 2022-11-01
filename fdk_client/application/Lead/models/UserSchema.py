"""Lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .PhoneNumber import PhoneNumber



from .Email import Email















from .Debug import Debug











class UserSchema(BaseSchema):
    #  swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    phone_numbers = fields.List(fields.Nested(PhoneNumber, required=False), required=False)
    
    emails = fields.List(fields.Nested(Email, required=False), required=False)
    
    gender = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    profile_pic_url = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    debug = fields.Nested(Debug, required=False)
    
    has_old_password_hash = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
