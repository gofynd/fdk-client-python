"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














from .BagsForReorderArticleAssignment import BagsForReorderArticleAssignment



class BagsForReorder(BaseSchema):
    #  swagger.json

    
    quantity = fields.Int(required=False)
    
    seller_id = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    article_assignment = fields.Nested(BagsForReorderArticleAssignment, required=False)
    
