"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class BagItemAttributes(BaseSchema):
    #  swagger.json

    
    item_code = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
