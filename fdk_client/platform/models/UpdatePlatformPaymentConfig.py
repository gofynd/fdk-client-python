"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class UpdatePlatformPaymentConfig(BaseSchema):
    # Payment swagger.json

    
    cod_amount_limit = fields.Int(required=False)
    
    payment_selection_lock = fields.Dict(required=False)
    
    methods = fields.Dict(required=False)
    
    anonymous_cod = fields.Boolean(required=False)
    
    cod_charges = fields.Int(required=False)
    

