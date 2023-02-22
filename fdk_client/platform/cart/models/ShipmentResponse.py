"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .CartProductInfo import CartProductInfo









from .ShipmentPromise import ShipmentPromise









class ShipmentResponse(BaseSchema):
    #  swagger.json

    
    fulfillment_type = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    box_type = fields.Str(required=False)
    
    dp_id = fields.Str(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    shipment_type = fields.Str(required=False)
    
    dp_options = fields.Dict(required=False)
    
    shipments = fields.Int(required=False)
    
