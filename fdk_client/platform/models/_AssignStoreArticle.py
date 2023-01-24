"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from ._ArticleQuery import _ArticleQuery

from ._ArticleAssignment import _ArticleAssignment








class _AssignStoreArticle(BaseSchema):
    # CompanyProfile swagger.json

    
    query = fields.Nested(_ArticleQuery, required=False)
    
    article_assignment = fields.Nested(_ArticleAssignment, required=False)
    
    group_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    

