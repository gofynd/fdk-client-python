"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .BagsForReorderArticleAssignment import BagsForReorderArticleAssignment







class BagsForReorder(BaseSchema):
    #  swagger.json

    
    store_id = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    article_assignment = fields.Nested(BagsForReorderArticleAssignment, required=False)
    
    seller_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
