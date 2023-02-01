"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .GSTDetailsData import GSTDetailsData

from .PlatformItem import PlatformItem













from .Prices import Prices




class BagUnit(BaseSchema):
    # Order swagger.json

    
    bag_id = fields.Int(required=False)
    
    gst = fields.Nested(GSTDetailsData, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    status = fields.Dict(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    item_quantity = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    can_cancel = fields.Boolean(required=False)
    

