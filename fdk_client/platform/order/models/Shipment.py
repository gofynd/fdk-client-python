"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .ProcessingDates import ProcessingDates





from .LineItem import LineItem



class Shipment(BaseSchema):
    #  swagger.json

    
    meta = fields.Dict(required=False)
    
    location_id = fields.Int(required=False)
    
    external_shipment_id = fields.Str(required=False)
    
    processing_dates = fields.Nested(ProcessingDates, required=False)
    
    priority = fields.Int(required=False)
    
    line_items = fields.List(fields.Nested(LineItem, required=False), required=False)
    
