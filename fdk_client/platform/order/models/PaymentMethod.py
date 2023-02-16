"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class PaymentMethod(BaseSchema):
    #  swagger.json

    
    collect_by = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    transaction_data = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
