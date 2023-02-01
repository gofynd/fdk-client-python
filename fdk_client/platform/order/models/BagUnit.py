"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Prices import Prices









from .GSTDetailsData import GSTDetailsData









from .PlatformItem import PlatformItem





class BagUnit(BaseSchema):
    #  swagger.json

    
    status = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    item_quantity = fields.Int(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    gst = fields.Nested(GSTDetailsData, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
