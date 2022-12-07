"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class FyndOrderIdList(BaseSchema):
    #  swagger.json

    
    fynd_order_id = fields.List(fields.Str(required=False), required=False)
    
