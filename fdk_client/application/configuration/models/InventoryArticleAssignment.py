"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ArticleAssignmentRule import ArticleAssignmentRule



class InventoryArticleAssignment(BaseSchema):
    #  swagger.json

    
    post_order_reassignment = fields.Boolean(required=False)
    
    rules = fields.Nested(ArticleAssignmentRule, required=False)
    
