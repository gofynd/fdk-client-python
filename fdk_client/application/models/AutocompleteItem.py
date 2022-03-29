"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Media import Media



from .Action import Action


class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    

