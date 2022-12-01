"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .OrderSchema import OrderSchema



class PosOrderById(BaseSchema):
    #  swagger.json

    
    order = fields.Nested(OrderSchema, required=False)
    
