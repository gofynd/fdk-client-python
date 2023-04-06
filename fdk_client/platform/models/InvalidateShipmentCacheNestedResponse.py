"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class InvalidateShipmentCacheNestedResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    

