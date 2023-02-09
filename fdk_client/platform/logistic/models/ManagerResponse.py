"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .MobileNo import MobileNo





class ManagerResponse(BaseSchema):
    #  swagger.json

    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(MobileNo, required=False)
    
    name = fields.Str(required=False)
    
