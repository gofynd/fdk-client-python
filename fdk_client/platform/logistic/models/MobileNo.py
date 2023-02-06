"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class MobileNo(BaseSchema):
    #  swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    
