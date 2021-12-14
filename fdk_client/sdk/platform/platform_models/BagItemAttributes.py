"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class BagItemAttributes(BaseSchema):
    # Order swagger.json

    
    item_code = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    

