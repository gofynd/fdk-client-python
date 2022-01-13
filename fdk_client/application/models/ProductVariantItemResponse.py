"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Action import Action



from .Media import Media














class ProductVariantItemResponse(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Nested(Action, required=False)
    
    uid = fields.Int(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    name = fields.Str(required=False)
    
    color_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
