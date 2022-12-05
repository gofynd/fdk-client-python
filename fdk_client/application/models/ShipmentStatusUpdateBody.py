"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Statuses1 import Statuses1




class ShipmentStatusUpdateBody(BaseSchema):
    # Order swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Nested(Statuses1, required=False), required=False)
    
    task = fields.Boolean(required=False)
    

