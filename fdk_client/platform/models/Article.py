"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Weight import Weight



from .ReturnConfig import ReturnConfig

from .Dimensions import Dimensions







from .Identifier import Identifier








class Article(BaseSchema):
    # Order swagger.json

    
    esp_modified = fields.Raw(required=False)
    
    _id = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    a_set = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    raw_meta = fields.Raw(required=False)
    
    uid = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    child_details = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    

