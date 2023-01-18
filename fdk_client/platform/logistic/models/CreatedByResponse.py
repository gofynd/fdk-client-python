"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CreatedByResponse(BaseSchema):
    #  swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
