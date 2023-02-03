"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Weight import Weight

















from .ReturnConfig import ReturnConfig







from .Dimensions import Dimensions



from .Identifier import Identifier





class Article(BaseSchema):
    #  swagger.json

    
    weight = fields.Nested(Weight, required=False)
    
    child_details = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    raw_meta = fields.Raw(required=False)
    
    code = fields.Str(required=False)
    
    a_set = fields.Dict(required=False)
    
    esp_modified = fields.Raw(required=False)
    
    uid = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    is_set = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    _id = fields.Str(required=False)
    
