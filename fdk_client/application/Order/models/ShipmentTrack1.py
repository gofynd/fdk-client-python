"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Track import Track



class ShipmentTrack1(BaseSchema):
    #  swagger.json

    
    results = fields.List(fields.Nested(Track, required=False), required=False)
    
