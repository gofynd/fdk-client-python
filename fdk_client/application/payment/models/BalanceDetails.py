"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class BalanceDetails(BaseSchema):
    #  swagger.json

    
    value = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    formatted_value = fields.Str(required=False)
    
