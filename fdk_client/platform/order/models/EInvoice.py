"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class EInvoice(BaseSchema):
    #  swagger.json

    
    irn = fields.Str(required=False)
    
    error_code = fields.Str(required=False)
    
    acknowledge_no = fields.Int(required=False)
    
    acknowledge_date = fields.Str(required=False)
    
    error_message = fields.Str(required=False)
    
    signed_qr_code = fields.Str(required=False)
    
    signed_invoice = fields.Str(required=False)
    
