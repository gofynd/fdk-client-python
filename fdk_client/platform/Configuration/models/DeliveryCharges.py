"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Charges import Charges



class DeliveryCharges(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    charges = fields.Nested(Charges, required=False)
    
