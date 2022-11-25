"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class BreakupValues(BaseSchema):
    #  swagger.json

    
    value = fields.Float(required=False)
    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
