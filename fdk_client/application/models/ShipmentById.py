"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentResponse import ShipmentResponse


class ShipmentById(BaseSchema):
    # Order swagger.json

    
    shipment = fields.Nested(ShipmentResponse, required=False)
    

