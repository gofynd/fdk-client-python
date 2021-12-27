"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema







from .ThirdLevelChild import ThirdLevelChild



from .ImageUrls import ImageUrls

from .ActionPage import ActionPage


class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(ActionPage, required=False)
    

