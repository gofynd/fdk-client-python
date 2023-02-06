"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Prices import Prices













from .GSTDetailsData import GSTDetailsData



from .PlatformItem import PlatformItem



class BagUnit(BaseSchema):
    #  swagger.json

    
    shipment_id = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    item_quantity = fields.Int(required=False)
    
    status = fields.Dict(required=False)
    
    gst = fields.Nested(GSTDetailsData, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
