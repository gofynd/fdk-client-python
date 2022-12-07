"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .DpConfiguration import DpConfiguration





from .PaymentInfo import PaymentInfo




class CreateOrderConfig(BaseSchema):
    # Order swagger.json

    
    logo_url = fields.Dict(required=False)
    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    
    lock_states = fields.Str(required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    shipment_assignment = fields.Str(required=False)
    

