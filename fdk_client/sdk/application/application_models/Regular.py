"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class Regular(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    

