"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class PaymentMethod(BaseSchema):
    #  swagger.json

    
    amount = fields.Float(required=False)
    
    name = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    transaction_data = fields.Dict(required=False)
    
    collect_by = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
