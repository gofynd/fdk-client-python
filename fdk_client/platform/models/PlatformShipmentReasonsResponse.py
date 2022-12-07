"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Reason import Reason


class PlatformShipmentReasonsResponse(BaseSchema):
    # Orders swagger.json

    
    success = fields.Boolean(required=False)
    
    reasons = fields.List(fields.Nested(Reason, required=False), required=False)
    

