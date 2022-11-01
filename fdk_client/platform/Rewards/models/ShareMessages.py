"""Rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class ShareMessages(BaseSchema):
    #  swagger.json

    
    email = fields.Str(required=False)
    
    facebook = fields.Str(required=False)
    
    fallback = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    messenger = fields.Str(required=False)
    
    sms = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    twitter = fields.Str(required=False)
    
    whatsapp = fields.Str(required=False)
    
