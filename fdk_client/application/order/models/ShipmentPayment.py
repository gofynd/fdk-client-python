"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ShipmentPayment(BaseSchema):
    #  swagger.json

    
    mop = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
