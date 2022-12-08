"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Reason import Reason



class PlatformShipmentReasonsResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    reasons = fields.List(fields.Nested(Reason, required=False), required=False)
    
