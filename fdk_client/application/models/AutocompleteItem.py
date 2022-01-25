"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Action1 import Action1





from .Media import Media


class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Nested(Action1, required=False)
    
    type = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    

