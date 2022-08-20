"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class ShipmentPayments(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    source_nickname = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    sp_id = fields.Int(required=False)
    
    display_priority = fields.Int(required=False)
    
    source = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    

