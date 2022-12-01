"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CallbackUrl import CallbackUrl



from .Methods import Methods



from .PaymentSelectionLock import PaymentSelectionLock















class AppPaymentConfig(BaseSchema):
    #  swagger.json

    
    callback_url = fields.Nested(CallbackUrl, required=False)
    
    methods = fields.Nested(Methods, required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    cod_amount_limit = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    anonymous_cod = fields.Boolean(required=False)
    
