"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Dimensions import Dimensions



from .Identifier import Identifier



from .ReturnConfig import ReturnConfig



from .Weight import Weight














class Article(BaseSchema):
    # Order swagger.json

    
    is_set = fields.Boolean(required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    child_details = fields.Dict(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    uid = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    raw_meta = fields.Raw(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    a_set = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    esp_modified = fields.Raw(required=False)
    
    code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    

