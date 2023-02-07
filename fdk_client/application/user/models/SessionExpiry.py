"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class SessionExpiry(BaseSchema):
    #  swagger.json

    
    duration = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    is_rolling = fields.Boolean(required=False)
    
