"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductListingAction import ProductListingAction





from .Media import Media







class AutocompleteItem(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(ProductListingAction, required=False)
    
    type = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    display = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
