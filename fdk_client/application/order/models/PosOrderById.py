"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderSchema1 import OrderSchema1



class PosOrderById(BaseSchema):
    #  swagger.json

    
    order = fields.Nested(OrderSchema1, required=False)
    
