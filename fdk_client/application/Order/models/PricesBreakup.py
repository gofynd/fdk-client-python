"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class PricesBreakup(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
