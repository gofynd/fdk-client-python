"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class AutocompletePageAction(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    params = fields.Dict(required=False)
    
