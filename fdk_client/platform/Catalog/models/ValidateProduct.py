"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ValidateProduct(BaseSchema):
    #  swagger.json

    
    valid = fields.Boolean(required=False)
    
