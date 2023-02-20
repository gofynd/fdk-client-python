"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Weight import Weight



from .Dimensions import Dimensions











from .Identifier import Identifier











from .ReturnConfig import ReturnConfig





class Article(BaseSchema):
    #  swagger.json

    
    a_set = fields.Dict(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    size = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    esp_modified = fields.Raw(required=False)
    
    child_details = fields.Dict(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    is_set = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    raw_meta = fields.Raw(required=False)
    
    _id = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    uid = fields.Str(required=False)
    
