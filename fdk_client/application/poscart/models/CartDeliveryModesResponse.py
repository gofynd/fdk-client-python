"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CartDeliveryModesResponse(BaseSchema):
    #  swagger.json

    
    available_modes = fields.List(fields.Str(required=False), required=False)
    
    pickup_stores = fields.List(fields.Int(required=False), required=False)
    
