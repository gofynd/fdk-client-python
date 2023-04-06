"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MobileNo import MobileNo






class ManagerResponse(BaseSchema):
    # Serviceability swagger.json

    
    mobile_no = fields.Nested(MobileNo, required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    

