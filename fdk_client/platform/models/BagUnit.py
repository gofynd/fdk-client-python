"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Prices import Prices

from .GSTDetailsData import GSTDetailsData



from .PlatformItem import PlatformItem








class BagUnit(BaseSchema):
    # Order swagger.json

    
    item_quantity = fields.Int(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    gst = fields.Nested(GSTDetailsData, required=False)
    
    status = fields.Dict(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    bag_id = fields.Int(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    

