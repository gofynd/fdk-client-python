"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Identifier import Identifier







from .Weight import Weight

from .Dimensions import Dimensions

from .ReturnConfig import ReturnConfig










class Article(BaseSchema):
    # Order swagger.json

    
    size = fields.Str(required=False)
    
    child_details = fields.Dict(required=False)
    
    raw_meta = fields.Raw(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    a_set = fields.Dict(required=False)
    
    esp_modified = fields.Raw(required=False)
    
    is_set = fields.Boolean(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    uid = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    

