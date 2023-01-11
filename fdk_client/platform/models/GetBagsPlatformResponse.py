"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page1 import Page1

from .BagDetailsPlatformResponse import BagDetailsPlatformResponse


class GetBagsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    page = fields.Nested(Page1, required=False)
    
    items = fields.List(fields.Nested(BagDetailsPlatformResponse, required=False), required=False)
    

