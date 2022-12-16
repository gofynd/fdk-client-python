"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderSchema1 import OrderSchema1



from .OrderPage import OrderPage



from .OrderFilters import OrderFilters



class OrderList1(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(OrderSchema1, required=False), required=False)
    
    page = fields.Nested(OrderPage, required=False)
    
    filters = fields.Nested(OrderFilters, required=False)
    
