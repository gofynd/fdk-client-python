"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class FollowerCountResponse(BaseSchema):
    #  swagger.json

    
    count = fields.Int(required=False)
    