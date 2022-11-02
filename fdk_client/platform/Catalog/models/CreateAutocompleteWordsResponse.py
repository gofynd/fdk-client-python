"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class CreateAutocompleteWordsResponse(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    results = fields.List(fields.Dict(required=False), required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    