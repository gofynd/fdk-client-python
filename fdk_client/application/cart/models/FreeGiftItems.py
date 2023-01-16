"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class FreeGiftItems(BaseSchema):
    #  swagger.json

    
    item_price_details = fields.Dict(required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_slug = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
