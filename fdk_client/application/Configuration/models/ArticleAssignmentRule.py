"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .StorePriorityRule import StorePriorityRule



class ArticleAssignmentRule(BaseSchema):
    #  swagger.json

    
    store_priority = fields.Nested(StorePriorityRule, required=False)
    
