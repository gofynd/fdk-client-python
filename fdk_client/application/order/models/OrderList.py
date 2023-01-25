"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderFilters import OrderFilters



from .OrderPage import OrderPage



from .OrderSchema import OrderSchema



class OrderList(BaseSchema):
    #  swagger.json

    
    filters = fields.Nested(OrderFilters, required=False)
    
    page = fields.Nested(OrderPage, required=False)
    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    
