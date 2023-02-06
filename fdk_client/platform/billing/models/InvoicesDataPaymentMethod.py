"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class InvoicesDataPaymentMethod(BaseSchema):
    #  swagger.json

    
    pg_payment_method_id = fields.Str(required=False)
    
