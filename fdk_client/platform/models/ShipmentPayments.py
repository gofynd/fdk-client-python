"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class ShipmentPayments(BaseSchema):
    # Order swagger.json

    
    sp_id = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    source_nickname = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    

