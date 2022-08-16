"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class ArticleDetails(BaseSchema):
    # Order swagger.json

    
    _id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    dimension = fields.Dict(required=False)
    
    brand_id = fields.Int(required=False)
    
    category = fields.Dict(required=False)
    
    attributes = fields.Dict(required=False)
    
    weight = fields.Dict(required=False)
    

