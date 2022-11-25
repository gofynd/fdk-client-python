"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .FreeGiftItemDetails import FreeGiftItemDetails









class AppliedFreeArticles(BaseSchema):
    #  swagger.json

    
    free_gift_item_details = fields.List(fields.Nested(FreeGiftItemDetails, required=False), required=False)
    
    article_id = fields.Str(required=False)
    
    quantity = fields.Float(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
