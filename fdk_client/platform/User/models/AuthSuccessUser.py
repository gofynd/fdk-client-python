"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .AuthSuccessUserDebug import AuthSuccessUserDebug





from .AuthSuccessUserEmails import AuthSuccessUserEmails



class AuthSuccessUser(BaseSchema):
    #  swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    debug = fields.Nested(AuthSuccessUserDebug, required=False)
    
    active = fields.Boolean(required=False)
    
    emails = fields.Nested(AuthSuccessUserEmails, required=False)
    
