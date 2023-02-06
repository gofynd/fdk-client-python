"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















from .RtoAddress import RtoAddress



class ShipmentInvoice(BaseSchema):
    #  swagger.json

    
    payment_type = fields.Str(required=False)
    
    updated_date = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    amount_to_collect = fields.Float(required=False)
    
    rto_address = fields.Nested(RtoAddress, required=False)
    
