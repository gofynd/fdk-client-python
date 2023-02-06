"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class BalanceDetails(BaseSchema):
    #  swagger.json

    
    currency = fields.Str(required=False)
    
    formatted_value = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
