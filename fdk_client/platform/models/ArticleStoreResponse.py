"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ArticleStoreResponse(BaseSchema):
    # Catalog swagger.json

    
    store_code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

