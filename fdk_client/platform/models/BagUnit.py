"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PlatformItem import PlatformItem

from .GSTDetailsData import GSTDetailsData

















from .Prices import Prices


class BagUnit(BaseSchema):
    # Order swagger.json

    
    item = fields.Nested(PlatformItem, required=False)
    
    gst = fields.Nested(GSTDetailsData, required=False)
    
    shipment_id = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    item_quantity = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    status = fields.Dict(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    bag_id = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    

