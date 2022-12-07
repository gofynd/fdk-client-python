"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ApefaceApiError(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
