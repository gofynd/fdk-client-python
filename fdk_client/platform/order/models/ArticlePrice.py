"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ArticlePrice(BaseSchema):
    #  swagger.json

    
    marked = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    effective = fields.Int(required=False)
    
    transfer = fields.Int(required=False)
    
