"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Media import Media





from .Action import Action








class ProductVariantItemResponse(BaseSchema):
    # Catalog swagger.json

    
    is_available = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    color = fields.Str(required=False)
    
    color_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

