"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class Login(BaseSchema):
    #  swagger.json

    
    password = fields.Boolean(required=False)
    
    otp = fields.Boolean(required=False)
    
