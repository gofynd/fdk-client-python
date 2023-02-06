"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ShipmentTimeStamp(BaseSchema):
    # Order swagger.json

    
    t_min = fields.Str(required=False)
    
    t_max = fields.Str(required=False)
    

