"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .UserEmail import UserEmail

from .UserPhoneNumber import UserPhoneNumber








class OwnerInfo(BaseSchema):

    
    _id = fields.Str(required=False)
    
    emails = fields.List(fields.Nested(UserEmail, required=False), required=False)
    
    phone_numbers = fields.List(fields.Nested(UserPhoneNumber, required=False), required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    profile_pic = fields.Str(required=False)
    

