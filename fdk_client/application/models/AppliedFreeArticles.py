"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .FreeGiftItemDetails import FreeGiftItemDetails


class AppliedFreeArticles(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Float(required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    free_gift_item_details = fields.List(fields.Nested(FreeGiftItemDetails, required=False), required=False)
    

