"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CouponDateMeta(BaseSchema):
    #  swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
