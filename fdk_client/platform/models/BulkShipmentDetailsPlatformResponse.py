"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Shipment import Shipment

from .Page1 import Page1


class BulkShipmentDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    page = fields.Nested(Page1, required=False)
    

