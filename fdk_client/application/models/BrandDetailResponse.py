"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ImageUrls import ImageUrls



from .Media import Media




class BrandDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    

