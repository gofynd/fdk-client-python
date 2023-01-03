"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class OrderDetails(BaseSchema):
    #  swagger.json

    
    fynd_order_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
