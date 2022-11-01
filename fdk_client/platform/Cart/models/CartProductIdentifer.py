"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CartProductIdentifer(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
