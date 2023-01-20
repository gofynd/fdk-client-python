"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .StoreIntegrationType import StoreIntegrationType









class ArticleStoreResponse(BaseSchema):
    #  swagger.json

    
    integration_type = fields.Nested(StoreIntegrationType, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
