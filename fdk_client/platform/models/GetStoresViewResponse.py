"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ItemResponse import ItemResponse

from .PageResponse import PageResponse


class GetStoresViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ItemResponse, required=False), required=False)
    
    page = fields.Nested(PageResponse, required=False)
    

