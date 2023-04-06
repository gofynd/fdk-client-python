"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .BagsForReorderArticleAssignment import BagsForReorderArticleAssignment






class BagsForReorder(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Int(required=False)
    
    seller_id = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    article_assignment = fields.Nested(BagsForReorderArticleAssignment, required=False)
    
    store_id = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    

