"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ArticleAssignment import ArticleAssignment





from .ArticleQuery import ArticleQuery





class AssignStoreArticle(BaseSchema):
    #  swagger.json

    
    group_id = fields.Str(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    meta = fields.Dict(required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    
    quantity = fields.Int(required=False)
    
