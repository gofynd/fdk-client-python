"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .DpConfiguration import DpConfiguration





from .PaymentInfo import PaymentInfo









class CreateOrderConfig(BaseSchema):
    #  swagger.json

    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    
    shipment_assignment = fields.Str(required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    lock_states = fields.Str(required=False)
    
    logo_url = fields.Dict(required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
