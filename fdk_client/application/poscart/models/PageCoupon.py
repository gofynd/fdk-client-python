"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class PageCoupon(BaseSchema):
    #  swagger.json

    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
    total_item_count = fields.Int(required=False)
    