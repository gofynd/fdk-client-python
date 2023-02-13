"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ShipmentPayments(BaseSchema):
    # Orders swagger.json

    
    logo = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    

