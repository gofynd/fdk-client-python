"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class OpenApiCheckoutResponse(BaseSchema):
    #  swagger.json

    
    order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    order_ref_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
