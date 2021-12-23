"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .ArticleQuery import ArticleQuery



from .ArticleAssignment import ArticleAssignment




class AssignStoreArticle(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    
    meta = fields.Dict(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    group_id = fields.Str(required=False)
    

