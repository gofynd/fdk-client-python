"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GST import GST









from .Prices import Prices





from .Item import Item


class BagUnit(BaseSchema):
    # Orders swagger.json

    
    gst = fields.Nested(GST, required=False)
    
    shipment_id = fields.Str(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    status = fields.Dict(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    item_quantity = fields.Int(required=False)
    
    bag_id = fields.Int(required=False)
    
    item = fields.Nested(Item, required=False)
    

