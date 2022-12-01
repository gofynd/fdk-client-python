"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PaymentGatewayConfig import PaymentGatewayConfig







class PaymentGatewayConfigRequest(BaseSchema):
    #  swagger.json

    
    aggregator_name = fields.Nested(PaymentGatewayConfig, required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
