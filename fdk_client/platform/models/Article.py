"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Weight import Weight

from .Identifier import Identifier









from .ReturnConfig import ReturnConfig





from .Dimensions import Dimensions






class Article(BaseSchema):
    # Order swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    raw_meta = fields.Raw(required=False)
    
    size = fields.Str(required=False)
    
    a_set = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    is_set = fields.Boolean(required=False)
    
    child_details = fields.Dict(required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    esp_modified = fields.Raw(required=False)
    
    uid = fields.Str(required=False)
    

