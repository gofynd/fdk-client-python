"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CheckResponse import CheckResponse


class UpdateShipmentLockResponse(BaseSchema):
    # OrderManage swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    check_response = fields.List(fields.Nested(CheckResponse, required=False), required=False)
    

