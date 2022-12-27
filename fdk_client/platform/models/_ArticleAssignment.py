"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class _ArticleAssignment(BaseSchema):
    # CompanyProfile swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    

