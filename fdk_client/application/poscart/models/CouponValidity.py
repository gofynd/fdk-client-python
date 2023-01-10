"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class CouponValidity(BaseSchema):
    #  swagger.json

    
    discount = fields.Float(required=False)
    
    valid = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    display_message_en = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
