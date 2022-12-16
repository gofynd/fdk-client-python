"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ShipmentPayment1(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    status = fields.Str(required=False)
    