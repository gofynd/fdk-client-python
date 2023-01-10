"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Media import Media



from .ProductListingAction import ProductListingAction







class AutocompleteItem(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    display = fields.Str(required=False)
    
