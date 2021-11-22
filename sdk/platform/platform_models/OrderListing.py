"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .OrderItems import OrderItems

from .Filters import Filters



from .PlatformOrderPage import PlatformOrderPage

from .AppliedFilters import AppliedFilters


class OrderListing(Schema):

    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    next_order_status = fields.Dict(required=False)
    
    page = fields.Nested(PlatformOrderPage, required=False)
    
    applied_filters = fields.Nested(AppliedFilters, required=False)
    

