"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Logo import Logo








class IntentApp(BaseSchema):
    # Payment swagger.json

    
    logos = fields.Nested(Logo, required=False)
    
    code = fields.Str(required=False)
    
    package_name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    

