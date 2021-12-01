"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class StatGroup(BaseSchema):

    
    key = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

