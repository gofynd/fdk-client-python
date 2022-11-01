"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ProductReturnConfig(BaseSchema):
    #  swagger.json

    
    on_same_store = fields.Boolean(required=False)
    
