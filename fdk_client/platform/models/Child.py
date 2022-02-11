"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SecondLevelChild import SecondLevelChild

from .Action import Action



from .ImageUrls import ImageUrls






class Child(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    action = fields.Nested(Action, required=False)
    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    

