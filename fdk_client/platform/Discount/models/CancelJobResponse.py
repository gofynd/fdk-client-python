"""Discount Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CancelJobResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    