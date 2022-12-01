"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class Email(BaseSchema):
    #  swagger.json

    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
