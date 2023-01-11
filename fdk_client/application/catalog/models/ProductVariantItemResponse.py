"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Media import Media





from .ProductListingAction import ProductListingAction









from .CustomMetaFields import CustomMetaFields









class ProductVariantItemResponse(BaseSchema):
    #  swagger.json

    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    color_name = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    value = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    color = fields.Str(required=False)
    
