"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CreatePaymentLinkMeta import CreatePaymentLinkMeta










class CreatePaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    external_order_id = fields.Str(required=False)
    
    meta = fields.Nested(CreatePaymentLinkMeta, required=False)
    
    amount = fields.Float(required=False)
    
    email = fields.Str(required=False)
    
    mobile_number = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

