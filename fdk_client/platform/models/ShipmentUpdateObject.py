"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ShipmentUpdateObject(BaseSchema):
    # Order swagger.json

    
    shipments = fields.Dict(required=False)
    

