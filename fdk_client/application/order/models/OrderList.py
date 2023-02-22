"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderFilters import OrderFilters



from .OrderSchema import OrderSchema



from .OrderPage import OrderPage



class OrderList(BaseSchema):
    #  swagger.json

    
    filters = fields.Nested(OrderFilters, required=False)
    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    
    page = fields.Nested(OrderPage, required=False)
    
