"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .StorePriority import StorePriority



class ArticleAssignmentRules(BaseSchema):
    #  swagger.json

    
    store_priority = fields.Nested(StorePriority, required=False)
    
