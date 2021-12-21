"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class APIError(BaseSchema):
    # Partner swagger.json

    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    

