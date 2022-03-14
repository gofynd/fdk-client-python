"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ShipmentPromise import ShipmentPromise



from .CartProductInfo import CartProductInfo








class ShipmentResponse(BaseSchema):
    # Cart swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    shipments = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
    dp_options = fields.Dict(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    box_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    dp_id = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    fulfillment_type = fields.Str(required=False)
    

