"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Identifier import Identifier



from .Dimensions import Dimensions





from .Weight import Weight





from .ReturnConfig import ReturnConfig












class Article(BaseSchema):
    # Order swagger.json

    
    identifiers = fields.Nested(Identifier, required=False)
    
    uid = fields.Str(required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    raw_meta = fields.Raw(required=False)
    
    size = fields.Str(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    esp_modified = fields.Raw(required=False)
    
    is_set = fields.Boolean(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    _id = fields.Str(required=False)
    
    child_details = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    a_set = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    

