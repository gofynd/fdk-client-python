"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ImageUrls import ImageUrls

from .Action import Action








class ThirdLevelChild(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(Action, required=False)
    
    slug = fields.Str(required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    

