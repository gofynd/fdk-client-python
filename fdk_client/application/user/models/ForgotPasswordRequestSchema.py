"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ForgotPasswordRequestSchema(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
