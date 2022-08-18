"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class UpdateShipmentStatusResponse1(BaseSchema):
    # Order swagger.json

    
    message = fields.List(fields.Dict(required=False), required=False)
    

