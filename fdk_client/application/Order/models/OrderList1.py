"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderItems import OrderItems



from .Filters import Filters



from .Page import Page



class OrderList1(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    page = fields.Nested(Page, required=False)
    
