"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .HistoryDict import HistoryDict



class ShipmentHistoryResponse(BaseSchema):
    #  swagger.json

    
    activity_history = fields.List(fields.Nested(HistoryDict, required=False), required=False)
    
