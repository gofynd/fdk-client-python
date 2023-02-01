"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .DpConfiguration import DpConfiguration





from .CreateChannelPaymentInfo import CreateChannelPaymentInfo



class CreateChannelConfig(BaseSchema):
    #  swagger.json

    
    lock_states = fields.List(fields.Str(required=False), required=False)
    
    logo_url = fields.Dict(required=False)
    
    shipment_assignment = fields.Str(required=False)
    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    payment_info = fields.Nested(CreateChannelPaymentInfo, required=False)
    
