"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class UserPhoneNumber(BaseSchema):
    #  swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    country_code = fields.Int(required=False)
    
    phone = fields.Str(required=False)
    
