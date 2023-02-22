"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from ._ArticleQuery import _ArticleQuery





from ._ArticleAssignment import _ArticleAssignment







class _AssignStoreArticle(BaseSchema):
    #  swagger.json

    
    query = fields.Nested(_ArticleQuery, required=False)
    
    quantity = fields.Int(required=False)
    
    article_assignment = fields.Nested(_ArticleAssignment, required=False)
    
    meta = fields.Dict(required=False)
    
    group_id = fields.Str(required=False)
    
