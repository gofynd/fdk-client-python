"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class PaymentMethods(BaseSchema):
    #  swagger.json

    
    collect_by = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
