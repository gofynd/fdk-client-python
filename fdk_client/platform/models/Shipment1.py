"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .ShipmentPricesDataSet import ShipmentPricesDataSet


class Shipment1(BaseSchema):
    # Orders swagger.json

    
    shipment_status = fields.Str(required=False)
    
    total_items = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    rtd_done = fields.Str(required=False)
    
    prices = fields.Nested(ShipmentPricesDataSet, required=False)
    

