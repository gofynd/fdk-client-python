"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ShipmentStatus(BaseSchema):
    # Orders swagger.json

    
    ops_status = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    hex_code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    actual_status = fields.Str(required=False)
    

