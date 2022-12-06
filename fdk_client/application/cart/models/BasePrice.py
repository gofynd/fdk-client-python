"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class BasePrice(BaseSchema):
    #  swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
