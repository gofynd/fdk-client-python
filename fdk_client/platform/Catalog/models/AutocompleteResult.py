"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .AutocompleteAction import AutocompleteAction



from .Media import Media



class AutocompleteResult(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(AutocompleteAction, required=False)
    
    logo = fields.Nested(Media, required=False)
    