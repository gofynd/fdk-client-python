"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class GetAutocompleteWordsData(BaseSchema):
    #  swagger.json

    
    results = fields.List(fields.Dict(required=False), required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
