"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .StatusesBodyResponse import StatusesBodyResponse



class ShipmentApplicationStatusResponse(BaseSchema):
    #  swagger.json

    
    statuses = fields.List(fields.Nested(StatusesBodyResponse, required=False), required=False)
    
