"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ItemPriceDetails import ItemPriceDetails




class FreeGiftItemDetails(BaseSchema):
    # Order swagger.json

    
    item_name = fields.Str(required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_price_details = fields.Nested(ItemPriceDetails, required=False)
    
    item_id = fields.Str(required=False)
    

