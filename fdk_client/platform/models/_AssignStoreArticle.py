"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from ._ArticleAssignment import _ArticleAssignment





from ._ArticleQuery import _ArticleQuery


class _AssignStoreArticle(BaseSchema):
    # CompanyProfile swagger.json

    
    quantity = fields.Int(required=False)
    
    article_assignment = fields.Nested(_ArticleAssignment, required=False)
    
    meta = fields.Dict(required=False)
    
    group_id = fields.Str(required=False)
    
    query = fields.Nested(_ArticleQuery, required=False)
    

