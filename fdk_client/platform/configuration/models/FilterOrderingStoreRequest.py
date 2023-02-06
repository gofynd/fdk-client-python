"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class FilterOrderingStoreRequest(BaseSchema):
    #  swagger.json

    
    all_stores = fields.Boolean(required=False)
    
    deployed_stores = fields.List(fields.Int(required=False), required=False)
    
    q = fields.Str(required=False)
    
