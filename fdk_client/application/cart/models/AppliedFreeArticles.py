"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .FreeGiftItem import FreeGiftItem









class AppliedFreeArticles(BaseSchema):
    #  swagger.json

    
    free_gift_item_details = fields.Nested(FreeGiftItem, required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
