"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .TrackShipmentResults import TrackShipmentResults



class TrackShipmentResponse(BaseSchema):
    #  swagger.json

    
    results = fields.List(fields.Nested(TrackShipmentResults, required=False), required=False)
    
