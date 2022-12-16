"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema


















from .ShipmentPromise import ShipmentPromise



from .CartProductInfo import CartProductInfo





class ShipmentResponse(BaseSchema):
    #  swagger.json

    
    dp_options = fields.Dict(required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    box_type = fields.Str(required=False)
    
    dp_id = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    shipment_type = fields.Str(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    shipments = fields.Int(required=False)
    