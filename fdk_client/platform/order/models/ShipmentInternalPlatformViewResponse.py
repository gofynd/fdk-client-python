"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ShipmentItem import ShipmentItem



from .FiltersInfo import FiltersInfo





class ShipmentInternalPlatformViewResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Dict(required=False)
    
    items = fields.List(fields.Nested(ShipmentItem, required=False), required=False)
    
    filters = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    applied_filters = fields.Dict(required=False)
    