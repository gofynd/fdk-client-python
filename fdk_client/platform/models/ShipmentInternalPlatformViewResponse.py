"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ShipmentItem import ShipmentItem

from .FiltersInfo import FiltersInfo




class ShipmentInternalPlatformViewResponse(BaseSchema):
    # Orders swagger.json

    
    applied_filters = fields.Dict(required=False)
    
    items = fields.List(fields.Nested(ShipmentItem, required=False), required=False)
    
    filters = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    page = fields.Dict(required=False)
    

