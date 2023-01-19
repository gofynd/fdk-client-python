"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class OrderDetails(BaseSchema):
    #  swagger.json

    
    created_at = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
