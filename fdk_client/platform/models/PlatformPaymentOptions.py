"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class PlatformPaymentOptions(BaseSchema):
    # Payment swagger.json

    
    callback_url = fields.Dict(required=False)
    
    enabled = fields.Boolean(required=False)
    
    cod_amount_limit = fields.Int(required=False)
    
    source = fields.Str(required=False)
    
    payment_selection_lock = fields.Dict(required=False)
    
    methods = fields.Dict(required=False)
    
    anonymous_cod = fields.Boolean(required=False)
    
    cod_charges = fields.Int(required=False)
    
    mode_of_payment = fields.Str(required=False)
    

