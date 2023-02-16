"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AutocompleteAction import AutocompleteAction



from .Media import Media







class AutocompleteResult(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(AutocompleteAction, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    display = fields.Str(required=False)
    
