"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderingStoreSelect import OrderingStoreSelect



class OrderingStoreSelectRequest(BaseSchema):
    #  swagger.json

    
    ordering_store = fields.Nested(OrderingStoreSelect, required=False)
    
