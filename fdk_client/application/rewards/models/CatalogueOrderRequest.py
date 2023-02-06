"""rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .RewardsArticle import RewardsArticle



class CatalogueOrderRequest(BaseSchema):
    #  swagger.json

    
    articles = fields.List(fields.Nested(RewardsArticle, required=False), required=False)
    
