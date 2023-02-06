"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .AutocompletePageAction import AutocompletePageAction



class AutocompleteAction(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(AutocompletePageAction, required=False)
    
