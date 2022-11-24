"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ShipmentTotalDetails(BaseSchema):
    # Order swagger.json

    
    total_price = fields.Float(required=False)
    
    pieces = fields.Float(required=False)
    
    sizes = fields.Float(required=False)
    

