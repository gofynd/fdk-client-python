"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .FiltersInfo import FiltersInfo



from .ShipmentItem import ShipmentItem





class ShipmentInternalPlatformViewResponse(BaseSchema):
    #  swagger.json

    
    applied_filters = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    items = fields.List(fields.Nested(ShipmentItem, required=False), required=False)
    
    page = fields.Dict(required=False)
    
