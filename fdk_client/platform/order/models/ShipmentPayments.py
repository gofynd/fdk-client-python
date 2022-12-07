"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ShipmentPayments(BaseSchema):
    #  swagger.json

    
    mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
