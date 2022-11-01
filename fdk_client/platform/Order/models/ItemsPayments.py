"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class ItemsPayments(BaseSchema):
    #  swagger.json

    
    display_priority = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    source_nickname = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
