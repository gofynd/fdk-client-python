"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PostOrder1(BaseSchema):
    # Cart swagger.json

    
    return_allowed = fields.Boolean(required=False)
    
    cancellation_allowed = fields.Boolean(required=False)
    
    partial_can_ret = fields.Boolean(required=False)
    

