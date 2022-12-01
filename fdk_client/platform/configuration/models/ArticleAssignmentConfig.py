"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ArticleAssignmentRules import ArticleAssignmentRules





class ArticleAssignmentConfig(BaseSchema):
    #  swagger.json

    
    rules = fields.Nested(ArticleAssignmentRules, required=False)
    
    post_order_reassignment = fields.Boolean(required=False)
    
