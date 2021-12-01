"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class StoreFilter(BaseSchema):

    
    include_tags = fields.List(fields.Str(required=False), required=False)
    
    exclude_tags = fields.List(fields.Str(required=False), required=False)
    
    query = fields.Dict(required=False)
    

