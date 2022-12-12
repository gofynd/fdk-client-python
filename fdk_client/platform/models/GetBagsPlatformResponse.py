"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagDetailsPlatformResponse import BagDetailsPlatformResponse

from .Page1 import Page1


class GetBagsPlatformResponse(BaseSchema):
    # Orders swagger.json

    
    items = fields.List(fields.Nested(BagDetailsPlatformResponse, required=False), required=False)
    
    page = fields.Nested(Page1, required=False)
    

