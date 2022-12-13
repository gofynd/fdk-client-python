"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PlatformItem import PlatformItem

from .Prices import Prices











from .GSTDetailsData import GSTDetailsData






class BagUnit(BaseSchema):
    # Order swagger.json

    
    ordering_channel = fields.Str(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    shipment_id = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    status = fields.Dict(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    gst = fields.Nested(GSTDetailsData, required=False)
    
    item_quantity = fields.Int(required=False)
    
    bag_id = fields.Int(required=False)
    

