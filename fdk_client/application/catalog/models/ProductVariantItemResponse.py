"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ProductListingAction import ProductListingAction



from .Media import Media





from .CustomMetaFields import CustomMetaFields











class ProductVariantItemResponse(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    color_name = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    color = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
