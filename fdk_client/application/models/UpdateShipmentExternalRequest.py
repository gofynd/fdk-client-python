"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class UpdateShipmentExternalRequest(BaseSchema):
    # Order swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Dict(required=False), required=False)
    

