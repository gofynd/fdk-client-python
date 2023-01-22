"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ArticleAssignment import ArticleAssignment





from .ArticleQuery import ArticleQuery



class AssignStoreArticle(BaseSchema):
    #  swagger.json

    
    meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    group_id = fields.Str(required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    