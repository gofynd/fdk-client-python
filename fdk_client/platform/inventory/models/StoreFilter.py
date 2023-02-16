"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class StoreFilter(BaseSchema):
    #  swagger.json

    
    include_tags = fields.List(fields.Str(required=False), required=False)
    
    exclude_tags = fields.List(fields.Str(required=False), required=False)
    
    query = fields.Dict(required=False)
    
