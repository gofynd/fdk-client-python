"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class FollowPostResponse(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
