"""Lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .HistoryTypeEnum import HistoryTypeEnum



class TicketHistoryPayload(BaseSchema):
    #  swagger.json

    
    value = fields.Dict(required=False)
    
    type = fields.Nested(HistoryTypeEnum, required=False)
    
