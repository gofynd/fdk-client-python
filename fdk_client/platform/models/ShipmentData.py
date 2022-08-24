"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentConfig import ShipmentConfig


class ShipmentData(BaseSchema):
    # Order swagger.json

    
    shipment_data = fields.Nested(ShipmentConfig, required=False)
    

