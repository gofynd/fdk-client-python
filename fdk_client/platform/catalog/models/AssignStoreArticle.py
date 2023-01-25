"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ArticleQuery import ArticleQuery



from .ArticleAssignment import ArticleAssignment







class AssignStoreArticle(BaseSchema):
    #  swagger.json

    
    meta = fields.Dict(required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    quantity = fields.Int(required=False)
    
    group_id = fields.Str(required=False)
    
