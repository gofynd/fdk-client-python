"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReasonsResponse import ReasonsResponse




class ShipmentReasonsResponse(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(ReasonsResponse, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

