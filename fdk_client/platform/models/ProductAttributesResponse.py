"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PageResponse import PageResponse

from .AttributeMasterSerializer import AttributeMasterSerializer


class ProductAttributesResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(PageResponse, required=False)
    
    items = fields.List(fields.Nested(AttributeMasterSerializer, required=False), required=False)
    

