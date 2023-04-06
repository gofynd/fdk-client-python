"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetInventories import GetInventories

from .Page import Page


class GetInventoriesResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetInventories, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

