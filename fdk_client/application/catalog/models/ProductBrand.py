"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .Media import Media



from .ProductListingAction import ProductListingAction





class ProductBrand(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    description = fields.Str(required=False)
    
