"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LineItem import LineItem







from .ProcessingDates import ProcessingDates




class Shipment(BaseSchema):
    # OrderManage swagger.json

    
    line_items = fields.List(fields.Nested(LineItem, required=False), required=False)
    
    priority = fields.Int(required=False)
    
    external_shipment_id = fields.Float(required=False)
    
    meta = fields.Dict(required=False)
    
    processing_dates = fields.Nested(ProcessingDates, required=False)
    
    location_id = fields.Int(required=False)
    

