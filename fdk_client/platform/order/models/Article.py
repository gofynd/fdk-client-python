"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .ReturnConfig import ReturnConfig

















from .Identifier import Identifier



from .Dimensions import Dimensions



from .Weight import Weight



class Article(BaseSchema):
    #  swagger.json

    
    raw_meta = fields.Raw(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    is_set = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    a_set = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    esp_modified = fields.Raw(required=False)
    
    child_details = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    weight = fields.Nested(Weight, required=False)
    
