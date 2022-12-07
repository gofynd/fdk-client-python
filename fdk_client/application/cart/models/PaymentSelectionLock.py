"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class PaymentSelectionLock(BaseSchema):
    #  swagger.json

    
    default_options = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    payment_identifier = fields.Str(required=False)
    