"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CartProductInfo import CartProductInfo









from .ShipmentPromise import ShipmentPromise




class ShipmentResponse(BaseSchema):
    # Cart swagger.json

    
    dp_options = fields.Dict(required=False)
    
    shipments = fields.Int(required=False)
    
    box_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    dp_id = fields.Str(required=False)
    

