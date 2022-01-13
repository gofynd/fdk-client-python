"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Media import Media

from .Action1 import Action1






class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(Action1, required=False)
    
    display = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
