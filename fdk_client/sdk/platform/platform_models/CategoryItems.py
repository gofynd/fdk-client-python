"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .ImageUrls import ImageUrls

from .Child import Child

from .Action import Action






class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    action = fields.Nested(Action, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

