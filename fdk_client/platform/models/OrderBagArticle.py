"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OrderBagArticle(BaseSchema):
    # Orders swagger.json

    
    uid = fields.Str(required=False)
    
    identifiers = fields.Dict(required=False)
    
    return_config = fields.Dict(required=False)
    

