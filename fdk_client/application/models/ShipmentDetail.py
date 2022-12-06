"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentBody import ShipmentBody


class ShipmentDetail(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Nested(ShipmentBody, required=False)
    

