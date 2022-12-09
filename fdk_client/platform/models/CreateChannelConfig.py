"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CreateChannelPaymentInfo import CreateChannelPaymentInfo





from .DpConfiguration import DpConfiguration


class CreateChannelConfig(BaseSchema):
    # OrderManage swagger.json

    
    logo_url = fields.Dict(required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    payment_info = fields.Nested(CreateChannelPaymentInfo, required=False)
    
    lock_states = fields.Str(required=False)
    
    shipment_assignment = fields.Str(required=False)
    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    

