"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ShipmentTotalDetails(BaseSchema):
    # Order swagger.json

    
    sizes = fields.Int(required=False)
    
    pieces = fields.Int(required=False)
    
    total_price = fields.Float(required=False)
    

