"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FiltersInfo import FiltersInfo





from .ShipmentItem import ShipmentItem


class ShipmentInternalPlatformViewResponse(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    page = fields.Dict(required=False)
    
    applied_filters = fields.Dict(required=False)
    
    items = fields.List(fields.Nested(ShipmentItem, required=False), required=False)
    

