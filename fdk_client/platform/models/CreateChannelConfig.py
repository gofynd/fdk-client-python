"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .DpConfiguration import DpConfiguration

from .CreateChannelPaymentInfo import CreateChannelPaymentInfo




class CreateChannelConfig(BaseSchema):
    # Order swagger.json

    
    location_reassignment = fields.Boolean(required=False)
    
    lock_states = fields.Str(required=False)
    
    logo_url = fields.Dict(required=False)
    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    
    payment_info = fields.Nested(CreateChannelPaymentInfo, required=False)
    
    shipment_assignment = fields.Str(required=False)
    

