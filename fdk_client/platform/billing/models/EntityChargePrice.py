"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class EntityChargePrice(BaseSchema):
    #  swagger.json

    
    amount = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
