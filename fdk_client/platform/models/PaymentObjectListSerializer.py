"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






































class PaymentObjectListSerializer(BaseSchema):
    # Payment swagger.json

    
    current_status = fields.Str(required=False)
    
    collected_by = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    all_status = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    payment_mode_identifier = fields.Str(required=False)
    
    refunded_by = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    user_object = fields.Dict(required=False)
    
    refund_object = fields.Dict(required=False)
    
    amount_in_paisa = fields.Str(required=False)
    
    aggregator_payment_object = fields.Dict(required=False)
    
    payment_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    

