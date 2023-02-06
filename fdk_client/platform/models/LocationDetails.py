"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ArticleDetails1 import ArticleDetails1




class LocationDetails(BaseSchema):
    # Order swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails1, required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    

