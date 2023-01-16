"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .SearchKeywordResult import SearchKeywordResult





class CreateSearchKeyword(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    result = fields.Nested(SearchKeywordResult, required=False)
    
    app_id = fields.Str(required=False)
    
