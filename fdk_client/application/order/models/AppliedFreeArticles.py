"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class AppliedFreeArticles(BaseSchema):
    #  swagger.json

    
    free_gift_item_details = fields.Dict(required=False)
    
    article_id = fields.Str(required=False)
    
    quantity = fields.Float(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
