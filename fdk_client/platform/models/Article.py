"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


























class Article(BaseSchema):
    # Order swagger.json

    
    esp_modified = fields.Raw(required=False)
    
    _id = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    is_set = fields.Raw(required=False)
    
    size = fields.Str(required=False)
    
    a_set = fields.Dict(required=False)
    
    identifiers = fields.Dict(required=False)
    
    raw_meta = fields.Raw(required=False)
    
    child_details = fields.Dict(required=False)
    

