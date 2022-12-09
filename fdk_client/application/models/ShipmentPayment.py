"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ShipmentPayment(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    mop = fields.Str(required=False)
    

