"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderFilters import OrderFilters



from .OrderSchema1 import OrderSchema1



from .OrderPage import OrderPage



class OrderList1(BaseSchema):
    #  swagger.json

    
    filters = fields.Nested(OrderFilters, required=False)
    
    items = fields.List(fields.Nested(OrderSchema1, required=False), required=False)
    
    page = fields.Nested(OrderPage, required=False)
    
