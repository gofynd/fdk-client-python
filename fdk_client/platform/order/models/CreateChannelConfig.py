"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DpConfiguration import DpConfiguration









from .CreateChannelPaymentInfo import CreateChannelPaymentInfo





class CreateChannelConfig(BaseSchema):
    #  swagger.json

    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    lock_states = fields.List(fields.Str(required=False), required=False)
    
    shipment_assignment = fields.Str(required=False)
    
    payment_info = fields.Nested(CreateChannelPaymentInfo, required=False)
    
    logo_url = fields.Dict(required=False)
    
