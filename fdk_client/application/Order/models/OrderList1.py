"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Filters import Filters



from .OrderItems import OrderItems



from .Page import Page



class OrderList1(BaseSchema):
    #  swagger.json

    
    filters = fields.Nested(Filters, required=False)
    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
