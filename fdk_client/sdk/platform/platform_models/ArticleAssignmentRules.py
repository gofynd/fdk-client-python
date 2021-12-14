"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .StorePriority import StorePriority


class ArticleAssignmentRules(BaseSchema):
    # Configuration swagger.json

    
    store_priority = fields.Nested(StorePriority, required=False)
    

