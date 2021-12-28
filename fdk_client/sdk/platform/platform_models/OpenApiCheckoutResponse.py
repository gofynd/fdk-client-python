"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class OpenApiCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    order_ref_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    

