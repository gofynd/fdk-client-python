"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagReasons import BagReasons


class ShipmentBagReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(BagReasons, required=False), required=False)
    

