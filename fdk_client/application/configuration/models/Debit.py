"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class Debit(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    auto_apply = fields.Boolean(required=False)
    
    strategy_channel = fields.Str(required=False)
    
