"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class OrderDetailsData(BaseSchema):
    #  swagger.json

    
    tax_details = fields.Dict(required=False)
    
    order_value = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    ordering_channel_logo = fields.Dict(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    order_date = fields.Str(required=False)
    
    cod_charges = fields.Str(required=False)
    
