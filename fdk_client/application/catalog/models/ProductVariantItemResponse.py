"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ProductListingAction import ProductListingAction











from .CustomMetaFields import CustomMetaFields



from .Media import Media





class ProductVariantItemResponse(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    color_name = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    name = fields.Str(required=False)
    
