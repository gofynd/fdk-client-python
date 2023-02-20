"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ShipmentPayments(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
