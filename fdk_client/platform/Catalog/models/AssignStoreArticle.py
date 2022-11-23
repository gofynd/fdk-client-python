"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ArticleQuery import ArticleQuery





from .ArticleAssignment import ArticleAssignment





class AssignStoreArticle(BaseSchema):
    #  swagger.json

    
    group_id = fields.Str(required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    
    quantity = fields.Int(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    meta = fields.Dict(required=False)
    
