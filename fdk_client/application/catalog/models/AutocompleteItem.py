"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductListingAction import ProductListingAction



from .Media import Media







class AutocompleteItem(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
