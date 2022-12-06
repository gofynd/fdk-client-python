"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .createOrderConfigResponse import createOrderConfigResponse



class CreateOrderConfigDataResponse(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(createOrderConfigResponse, required=False), required=False)
    
