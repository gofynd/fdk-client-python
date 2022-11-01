"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CreateUserSessionRequestSchema(BaseSchema):
    #  swagger.json

    
    domain = fields.Str(required=False)
    
    max_age = fields.Float(required=False)
    
    user_id = fields.Str(required=False)
    
