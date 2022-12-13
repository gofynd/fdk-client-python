"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class FreeGiftItem(BaseSchema):
    # Cart swagger.json

    
    item_slug = fields.Str(required=False)
    
    item_price_details = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    item_name = fields.Str(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_brand_name = fields.Str(required=False)
    

