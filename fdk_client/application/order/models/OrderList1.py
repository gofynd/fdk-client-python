"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderPage import OrderPage



from .OrderSchema1 import OrderSchema1



from .OrderFilters import OrderFilters



class OrderList1(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(OrderPage, required=False)
    
    items = fields.List(fields.Nested(OrderSchema1, required=False), required=False)
    
    filters = fields.Nested(OrderFilters, required=False)
    
