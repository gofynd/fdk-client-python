"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class FollowPostResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
