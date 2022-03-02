"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Media import Media





from .ImageUrls import ImageUrls





from .Action import Action




class BrandItem(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    discount = fields.Str(required=False)
    

