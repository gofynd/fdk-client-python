"""Discount Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class BadRequestObject(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
