"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OrderPriority(BaseSchema):
    #  swagger.json

    
    affiliate_priority_code = fields.Str(required=False)
    
    fulfilment_priority_text = fields.Str(required=False)
    
    fulfilment_priority = fields.Int(required=False)
    
