"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class ShipmentPayment(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

