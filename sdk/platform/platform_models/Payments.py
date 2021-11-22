"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




















class Payments(Schema):

    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    source_nickname = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    mode = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    

