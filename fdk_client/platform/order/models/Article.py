"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Dimensions import Dimensions



from .Weight import Weight











from .Identifier import Identifier









from .ReturnConfig import ReturnConfig



class Article(BaseSchema):
    #  swagger.json

    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    esp_modified = fields.Raw(required=False)
    
    is_set = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    a_set = fields.Dict(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    raw_meta = fields.Raw(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    child_details = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
