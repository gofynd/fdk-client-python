"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class PaymentGatewayConfigResponse(BaseSchema):
    #  swagger.json

    
    created = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    aggregators = fields.List(fields.Dict(required=False), required=False)
    
    excluded_fields = fields.List(fields.Str(required=False), required=False)
    
    display_fields = fields.List(fields.Str(required=False), required=False)
    
