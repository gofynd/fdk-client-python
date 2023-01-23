"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ArticleStoreResponse(BaseSchema):
    #  swagger.json

    
    store_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
