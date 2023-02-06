"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CartProductIdentifer(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
