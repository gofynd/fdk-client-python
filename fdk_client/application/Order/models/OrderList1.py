"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderPage import OrderPage



from .OrderFilters import OrderFilters



from .OrderSchema1 import OrderSchema1



class OrderList1(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(OrderPage, required=False)
    
    filters = fields.Nested(OrderFilters, required=False)
    
    items = fields.List(fields.Nested(OrderSchema1, required=False), required=False)
    
