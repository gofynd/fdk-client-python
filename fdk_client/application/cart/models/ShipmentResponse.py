"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












from .CartProductInfo import CartProductInfo





from .ShipmentPromise import ShipmentPromise









class ShipmentResponse(BaseSchema):
    #  swagger.json

    
    shipment_type = fields.Str(required=False)
    
    box_type = fields.Str(required=False)
    
    shipments = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    dp_options = fields.Dict(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    dp_id = fields.Str(required=False)
    