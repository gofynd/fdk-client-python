"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ArticleDetails import ArticleDetails







class LocationDetails(BaseSchema):
    #  swagger.json

    
    articles = fields.List(fields.Nested(ArticleDetails, required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
