"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class UnDeleteUserRequestSchema(BaseSchema):
    #  swagger.json

    
    user_id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    reason_id = fields.Str(required=False)
    
