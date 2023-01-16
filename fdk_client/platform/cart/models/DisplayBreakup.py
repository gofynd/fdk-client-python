"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class DisplayBreakup(BaseSchema):
    #  swagger.json

    
    value = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
    currency_code = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
