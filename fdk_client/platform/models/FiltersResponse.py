"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Filters import Filters

from .Filters import Filters


class FiltersResponse(BaseSchema):
    # Orders swagger.json

    
    delivery_partners = fields.List(fields.Nested(Filters, required=False), required=False)
    
    channels = fields.List(fields.Nested(Filters, required=False), required=False)
    

