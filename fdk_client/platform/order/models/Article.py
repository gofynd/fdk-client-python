"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ReturnConfig import ReturnConfig





from .Identifier import Identifier







from .Weight import Weight





from .Dimensions import Dimensions















class Article(BaseSchema):
    #  swagger.json

    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    raw_meta = fields.Raw(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    esp_modified = fields.Raw(required=False)
    
    child_details = fields.Dict(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    a_set = fields.Dict(required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    uid = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
