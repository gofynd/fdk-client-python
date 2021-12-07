"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class OpenApiErrorResponse(BaseSchema):

    
    message = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    

