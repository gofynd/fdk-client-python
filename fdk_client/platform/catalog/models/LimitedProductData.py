"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




























class LimitedProductData(BaseSchema):
    #  swagger.json

    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    price = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
