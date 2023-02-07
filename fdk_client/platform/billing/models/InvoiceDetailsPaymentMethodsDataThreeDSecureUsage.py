"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class InvoiceDetailsPaymentMethodsDataThreeDSecureUsage(BaseSchema):
    #  swagger.json

    
    supported = fields.Boolean(required=False)
    
