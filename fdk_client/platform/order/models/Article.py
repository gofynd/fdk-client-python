"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Identifier import Identifier





from .ReturnConfig import ReturnConfig









from .Dimensions import Dimensions







from .Weight import Weight





class Article(BaseSchema):
    #  swagger.json

    
    child_details = fields.Dict(required=False)
    
    esp_modified = fields.Raw(required=False)
    
    a_set = fields.Dict(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    raw_meta = fields.Raw(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    _id = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    is_set = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    size = fields.Str(required=False)
    
