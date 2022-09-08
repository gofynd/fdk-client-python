"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Bag import Bag

from .Page import Page


class GetBagsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(Bag, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

