"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .PaymentInfo import PaymentInfo





from .DpConfiguration import DpConfiguration







class CreateOrderConfig(BaseSchema):
    #  swagger.json

    
    lock_states = fields.Str(required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    
    logo_url = fields.Dict(required=False)
    
    shipment_assignment = fields.Str(required=False)
    
