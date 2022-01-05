"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ResponseVerifyOTPShipment(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    

