"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class SuccessResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    