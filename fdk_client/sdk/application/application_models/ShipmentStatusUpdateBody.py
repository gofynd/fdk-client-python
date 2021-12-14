"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .StatusesBody import StatusesBody




class ShipmentStatusUpdateBody(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatusesBody, required=False), required=False)
    
    force_transition = fields.Boolean(required=False)
    

