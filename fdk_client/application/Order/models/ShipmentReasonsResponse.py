"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ReasonsResponse import ReasonsResponse



class ShipmentReasonsResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    reasons = fields.List(fields.Nested(ReasonsResponse, required=False), required=False)
    
