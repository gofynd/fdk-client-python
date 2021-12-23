"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ArticleAssignment(BaseSchema):
    # Order swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    

