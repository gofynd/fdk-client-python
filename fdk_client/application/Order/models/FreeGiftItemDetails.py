"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ItemPriceDetails import ItemPriceDetails









class FreeGiftItemDetails(BaseSchema):
    #  swagger.json

    
    item_price_details = fields.Nested(ItemPriceDetails, required=False)
    
    item_name = fields.Str(required=False)
    
    item_id = fields.Str(required=False)
    
    item_brand_name = fields.Str(required=False)
    
