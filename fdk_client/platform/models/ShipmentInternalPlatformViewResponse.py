"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentItem import ShipmentItem



from .FiltersInfo import FiltersInfo




class ShipmentInternalPlatformViewResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(ShipmentItem, required=False), required=False)
    
    page = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    applied_filters = fields.Dict(required=False)
    

