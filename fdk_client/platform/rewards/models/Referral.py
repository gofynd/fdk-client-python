"""rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Referral(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
