"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentidResponse import ShipmentidResponse


class ShipmentsResponse(BaseSchema):
    # OrderManage swagger.json

    
    shipment_id = fields.Nested(ShipmentidResponse, required=False)
    

