"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ShipmentTimeStamp(BaseSchema):
    # Orders swagger.json

    
    t_max = fields.Str(required=False)
    
    t_min = fields.Str(required=False)
    

