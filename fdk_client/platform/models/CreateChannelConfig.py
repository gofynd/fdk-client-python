"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CreateChannelPaymentInfo import CreateChannelPaymentInfo

from .DpConfiguration import DpConfiguration


class CreateChannelConfig(BaseSchema):
    # Order swagger.json

    
    logo_url = fields.Dict(required=False)
    
    lock_states = fields.List(fields.Str(required=False), required=False)
    
    shipment_assignment = fields.Str(required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    payment_info = fields.Nested(CreateChannelPaymentInfo, required=False)
    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    

