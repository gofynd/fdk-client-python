"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentsResponse import ShipmentsResponse


class StatuesResponse(BaseSchema):
    # Order swagger.json

    
    shipments = fields.Nested(ShipmentsResponse, required=False)
    

