"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PlatformAddress import PlatformAddress


class PlatformGetAddressesResponse(BaseSchema):
    # Cart swagger.json

    
    address = fields.List(fields.Nested(PlatformAddress, required=False), required=False)
    

