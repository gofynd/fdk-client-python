"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SearchKeywordResult(BaseSchema):
    #  swagger.json

    
    query = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
