"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CouponDateMeta(BaseSchema):
    #  swagger.json

    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
