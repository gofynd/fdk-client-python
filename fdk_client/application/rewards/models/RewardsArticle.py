"""rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class RewardsArticle(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    points = fields.Float(required=False)
    
    price = fields.Float(required=False)
    
