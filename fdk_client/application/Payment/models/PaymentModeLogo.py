"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class PaymentModeLogo(BaseSchema):
    #  swagger.json

    
    small = fields.Str(required=False)
    
    large = fields.Str(required=False)
    
