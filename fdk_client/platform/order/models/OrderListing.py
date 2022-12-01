"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OrderItems import OrderItems



from .Filters import Filters





from .PlatformOrderPage import PlatformOrderPage



from .AppliedFilters import AppliedFilters



class OrderListing(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    next_order_status = fields.Dict(required=False)
    
    page = fields.Nested(PlatformOrderPage, required=False)
    
    applied_filters = fields.Nested(AppliedFilters, required=False)
    
