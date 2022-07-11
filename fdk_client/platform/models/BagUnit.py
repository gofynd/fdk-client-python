"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Prices import Prices









from .GST import GST



from .Item import Item


class BagUnit(BaseSchema):
    # Orders swagger.json

    
    total_shipment_bags = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    status = fields.Dict(required=False)
    
    bag_id = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    gst = fields.Nested(GST, required=False)
    
    item_quantity = fields.Int(required=False)
    
    item = fields.Nested(Item, required=False)
    

