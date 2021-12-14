"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema





from .OS import OS


class Device(BaseSchema):
    # Configuration swagger.json

    
    build = fields.Int(required=False)
    
    model = fields.Str(required=False)
    
    os = fields.Nested(OS, required=False)
    

