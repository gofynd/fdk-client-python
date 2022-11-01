"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class RegistrationPageFeature(BaseSchema):
    #  swagger.json

    
    ask_store_address = fields.Boolean(required=False)
    
