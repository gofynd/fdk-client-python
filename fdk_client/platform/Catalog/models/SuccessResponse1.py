"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SuccessResponse1(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    