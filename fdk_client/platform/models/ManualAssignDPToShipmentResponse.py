"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ManualAssignDPToShipmentResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Str(required=False)
    
    errors = fields.List(fields.Str(required=False), required=False)
    

