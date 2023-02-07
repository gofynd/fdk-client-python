"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ProductPublish1(BaseSchema):
    #  swagger.json

    
    product_online_date = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
