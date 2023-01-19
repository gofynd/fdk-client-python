"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .BagsForReorderArticleAssignment import BagsForReorderArticleAssignment













class BagsForReorder(BaseSchema):
    #  swagger.json

    
    article_assignment = fields.Nested(BagsForReorderArticleAssignment, required=False)
    
    quantity = fields.Int(required=False)
    
    seller_id = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
