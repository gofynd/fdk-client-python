"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ArticleDetails(BaseSchema):
    # Orders swagger.json

    
    status = fields.Dict(required=False)
    

