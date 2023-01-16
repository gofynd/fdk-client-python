"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CartCurrency(BaseSchema):
    #  swagger.json

    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    