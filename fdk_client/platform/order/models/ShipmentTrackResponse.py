"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShipmentTrackResponseBagListItem import ShipmentTrackResponseBagListItem







class ShipmentTrackResponse(BaseSchema):
    #  swagger.json

    
    bag_list = fields.List(fields.Nested(ShipmentTrackResponseBagListItem, required=False), required=False)
    
    message = fields.Str(required=False)
    
    order_value = fields.Int(required=False)
    
