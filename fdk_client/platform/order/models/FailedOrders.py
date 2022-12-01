"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FailOrder import FailOrder



class FailedOrders(BaseSchema):
    #  swagger.json

    
    orders = fields.Nested(FailOrder, required=False)
    
