"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UpdateShipmentResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Boolean(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
    final_state = fields.Dict(required=False)
    

