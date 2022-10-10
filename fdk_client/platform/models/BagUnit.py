"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Item import Item



from .GST import GST

from .Prices import Prices








class BagUnit(BaseSchema):
    # Orders swagger.json

    
    bag_id = fields.Int(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    item = fields.Nested(Item, required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    gst = fields.Nested(GST, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    status = fields.Dict(required=False)
    
    item_quantity = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    

