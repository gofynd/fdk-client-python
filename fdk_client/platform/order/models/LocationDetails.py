"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ArticleDetails1 import ArticleDetails1





class LocationDetails(BaseSchema):
    #  swagger.json

    
    fulfillment_type = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails1, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    
