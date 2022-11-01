"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class ErrorResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Str(required=False)
    
