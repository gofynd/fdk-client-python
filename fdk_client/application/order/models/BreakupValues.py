"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class BreakupValues(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
