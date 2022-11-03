"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OrderBagArticle(BaseSchema):
    # Orders swagger.json

    
    identifiers = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    

