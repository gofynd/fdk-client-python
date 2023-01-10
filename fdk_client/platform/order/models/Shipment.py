"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LineItem import LineItem



from .ProcessingDates import ProcessingDates











class Shipment(BaseSchema):
    #  swagger.json

    
    line_items = fields.List(fields.Nested(LineItem, required=False), required=False)
    
    processing_dates = fields.Nested(ProcessingDates, required=False)
    
    external_shipment_id = fields.Float(required=False)
    
    priority = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    location_id = fields.Int(required=False)
    
