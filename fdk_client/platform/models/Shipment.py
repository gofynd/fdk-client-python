"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProcessingDates import ProcessingDates





from .LineItem import LineItem


class Shipment(BaseSchema):
    # Order swagger.json

    
    location_id = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    processing_dates = fields.Nested(ProcessingDates, required=False)
    
    external_shipment_id = fields.Float(required=False)
    
    priority = fields.Int(required=False)
    
    line_items = fields.List(fields.Nested(LineItem, required=False), required=False)
    

