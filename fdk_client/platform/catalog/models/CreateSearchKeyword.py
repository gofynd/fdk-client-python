"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .SearchKeywordResult import SearchKeywordResult







class CreateSearchKeyword(BaseSchema):
    #  swagger.json

    
    app_id = fields.Str(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    result = fields.Nested(SearchKeywordResult, required=False)
    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
