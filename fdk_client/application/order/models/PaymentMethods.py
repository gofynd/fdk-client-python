"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class PaymentMethods(BaseSchema):
    #  swagger.json

    
    refund_by = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    collect_by = fields.Str(required=False)
    
