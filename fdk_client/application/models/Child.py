"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Action import Action







from .ImageUrls import ImageUrls



from .SecondLevelChild import SecondLevelChild


class Child(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    

