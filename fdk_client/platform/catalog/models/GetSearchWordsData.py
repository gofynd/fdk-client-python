"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class GetSearchWordsData(BaseSchema):
    #  swagger.json

    
    result = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
