"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .StatuesResponse import StatuesResponse



class StatusUpdateInternalResponse(BaseSchema):
    #  swagger.json

    
    statuses = fields.List(fields.Nested(StatuesResponse, required=False), required=False)
    
