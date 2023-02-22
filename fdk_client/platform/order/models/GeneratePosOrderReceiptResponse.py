"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class GeneratePosOrderReceiptResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    invoice_receipt = fields.Str(required=False)
    
    payment_receipt = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
