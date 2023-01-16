"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class PaymentMethod(BaseSchema):
    #  swagger.json

    
    transaction_data = fields.Dict(required=False)
    
    refund_by = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    name = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    collect_by = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    