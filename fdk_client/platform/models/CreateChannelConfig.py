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
    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    
    shipment_assignment = fields.Str(required=False)
    
    payment_info = fields.Nested(CreateChannelPaymentInfo, required=False)
    
    logo_url = fields.Dict(required=False)
    
    lock_states = fields.List(fields.Str(required=False), required=False)
    

