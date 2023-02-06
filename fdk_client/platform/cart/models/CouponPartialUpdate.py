"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CouponSchedule import CouponSchedule





class CouponPartialUpdate(BaseSchema):
    #  swagger.json

    
    schedule = fields.Nested(CouponSchedule, required=False)
    
    archive = fields.Boolean(required=False)
    
