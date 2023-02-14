"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Media import Media



from .AutocompleteAction import AutocompleteAction







class AutocompleteResult(BaseSchema):
    #  swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(AutocompleteAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    display = fields.Str(required=False)
    
