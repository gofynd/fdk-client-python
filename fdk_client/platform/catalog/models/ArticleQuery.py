"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ArticleQuery(BaseSchema):
    #  swagger.json

    
    item_id = fields.Int(required=False)
    
    ignored_stores = fields.List(fields.Int(required=False), required=False)
    
    size = fields.Str(required=False)
    
