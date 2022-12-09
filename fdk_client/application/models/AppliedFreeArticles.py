"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class AppliedFreeArticles(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Float(required=False)
    
    free_gift_item_details = fields.Dict(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    

