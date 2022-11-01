"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .StorePriorityRule import StorePriorityRule



class ArticleAssignmentRule(BaseSchema):
    #  swagger.json

    
    store_priority = fields.Nested(StorePriorityRule, required=False)
    
