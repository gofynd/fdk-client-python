"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Action import Action





from .Media import Media


class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Nested(Action, required=False)
    
    display = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    

