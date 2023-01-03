"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShipmentTrackingResultsResponse import ShipmentTrackingResultsResponse





class ShipmentTrackingResponse(BaseSchema):
    #  swagger.json

    
    results = fields.Nested(ShipmentTrackingResultsResponse, required=False)
    
    meta = fields.Dict(required=False)
    
