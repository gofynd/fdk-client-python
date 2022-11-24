"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OrderBagArticle(BaseSchema):
    # Order swagger.json

    
    return_config = fields.Dict(required=False)
    
    identifiers = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    

