"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderStatuses import OrderStatuses



class OrderFilters(BaseSchema):
    #  swagger.json

    
    statuses = fields.List(fields.Nested(OrderStatuses, required=False), required=False)
    
