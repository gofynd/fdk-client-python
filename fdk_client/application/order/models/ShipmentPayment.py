"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class ShipmentPayment(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    mop = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
