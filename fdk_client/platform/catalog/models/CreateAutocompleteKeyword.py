"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .AutocompleteResult import AutocompleteResult







class CreateAutocompleteKeyword(BaseSchema):
    #  swagger.json

    
    app_id = fields.Str(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    results = fields.List(fields.Nested(AutocompleteResult, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
