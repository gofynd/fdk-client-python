"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProcessingDates import ProcessingDates







from .LineItem import LineItem




class Shipment(BaseSchema):
    # Order swagger.json

    
    processing_dates = fields.Nested(ProcessingDates, required=False)
    
    meta = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    external_shipment_id = fields.Float(required=False)
    
    line_items = fields.List(fields.Nested(LineItem, required=False), required=False)
    
    location_id = fields.Int(required=False)
    

