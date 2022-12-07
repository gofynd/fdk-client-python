"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class UserInfo(BaseSchema):
    #  swagger.json

    
    gender = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
