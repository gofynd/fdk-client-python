"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .FreeGiftItem import FreeGiftItem




class AppliedFreeArticles(BaseSchema):
    # Cart swagger.json

    
    article_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    free_gift_item_detials = fields.List(fields.Nested(FreeGiftItem, required=False), required=False)
    
    parent_item_identifier = fields.Str(required=False)
    

