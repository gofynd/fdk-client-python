"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FiltersInfo import FiltersInfo

from .FiltersInfo import FiltersInfo


class FiltersResponse(BaseSchema):
    # Order swagger.json

    
    channels = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    delivery_partners = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    

