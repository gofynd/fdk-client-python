"""configuration Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema




















class Currency(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    decimal_digits = fields.Int(required=False)
    
    symbol = fields.Str(required=False)
    
