"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Prices import Prices





from .PlatformItem import PlatformItem









from .GSTDetailsData import GSTDetailsData





class BagUnit(BaseSchema):
    #  swagger.json

    
    ordering_channel = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    bag_id = fields.Int(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    item_quantity = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    gst = fields.Nested(GSTDetailsData, required=False)
    
    status = fields.Dict(required=False)
    
