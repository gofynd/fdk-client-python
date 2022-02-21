"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Logo import Logo




class IntentApp(BaseSchema):
    # Payment swagger.json

    
    package_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    logos = fields.Nested(Logo, required=False)
    
    display_name = fields.Str(required=False)
    

