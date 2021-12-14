"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class ShipmentTotalDetails(BaseSchema):
    # Order swagger.json

    
    total_price = fields.Float(required=False)
    
    sizes = fields.Int(required=False)
    
    pieces = fields.Int(required=False)
    

