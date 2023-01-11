"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from ._ArticleAssignment import _ArticleAssignment





from ._ArticleQuery import _ArticleQuery



class _AssignStoreArticle(BaseSchema):
    #  swagger.json

    
    meta = fields.Dict(required=False)
    
    group_id = fields.Str(required=False)
    
    article_assignment = fields.Nested(_ArticleAssignment, required=False)
    
    quantity = fields.Int(required=False)
    
    query = fields.Nested(_ArticleQuery, required=False)
    
